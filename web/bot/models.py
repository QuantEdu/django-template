# Django core
from django.contrib.postgres.fields import ArrayField
from django.db import models

from crm.users.models import User
from crm.social.models import UserSocialAuth
from lms.lessons.models import Lesson

from . import vkapi


class DialogManager(models.Manager):
    def create_dialog(self, user_vk_id, first_name, last_name):
        # Найти пользователя , собрать дефолтные задачи, выставить стэйт
        try:
            vk_auth = UserSocialAuth.objects.get(uid=user_vk_id, provider='vk')
            user = vk_auth.user
            dialog = self.create(user=user, state='DEFAULT_BOT_STATE')
            return dialog
        except UserSocialAuth.DoesNotExist:
            # TODO сделать нормально
            try:
                new_user = User.objects.get(email=str(user_vk_id) + '@email.ru')
            except User.DoesNotExist:
                try:
                    new_user = User.objects.create_user(email=str(user_vk_id) + '@email.ru',
                                                    first_name=first_name,
                                                    last_name=last_name)
                except Exception as e:
                    print('try to create user without name\n', e)
                    new_user = User.objects.create_user(email=str(user_vk_id) + '@email.ru')

            # TODO получить данные пользователя от  vk по  vk_id


            vk_auth = UserSocialAuth.objects.create(
                uid=user_vk_id,
                user=new_user,
                provider='vk'
            )
            vk_auth.save()
            dialog = self.create(user=new_user, state='DEFAULT_BOT_STATE')
            return dialog

        except Exception:
            # TODO посмотреть исключения
            raise ValueError('User with id {} not found'.format(user_vk_id))


class Dialog(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    objects = DialogManager()

    STATES = (
        ('DEFAULT_BOT_STATE', 'Wait for any command'),
        ('NEED_NEXT_BOT_STATE', 'Wait for answer the question "Need the next block?"'),
        ('WAIT_ANSWER_BOT_STATE', 'Wait for current block answer'),
    )

    state = models.CharField(choices=STATES, max_length=128)

    blocks_ids = ArrayField(
        models.IntegerField(),
        verbose_name='Массив из id блоков',
        blank=True,
        default=[]
    )

    current_block_pointer = models.IntegerField('block pointer', default=0)

    # check state functions
    def is_state_default(self):
        return self.state == 'DEFAULT_BOT_STATE'

    def is_state_need_next(self):
        return self.state == 'NEED_NEXT_BOT_STATE'

    def is_state_need_answer(self):
        return self.state == 'WAIT_ANSWER_BOT_STATE'

    # change state functions
    def change_state_to_default(self):
        self.state = 'DEFAULT_BOT_STATE'
        self.save()

    def change_state_to_need_next(self):
        self.state = 'NEED_NEXT_BOT_STATE'
        self.save()

    def change_state_to_need_answer(self):
        self.state = 'WAIT_ANSWER_BOT_STATE'
        self.save()

    def update_pointer(self):
        """Перемещает указатель на следующую задачу в списке"""
        if self.current_block_pointer < len(self.blocks_ids) - 1:
            self.current_block_pointer += 1
            self.save()
            return self.current_block_pointer
        return None


class BotService(models.Model):
    start = models.DateTimeField()
    end = models.DateField()
    course = models.ForeignKey(Lesson, verbose_name="Курс", on_delete=models.CASCADE)