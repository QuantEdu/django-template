# Django core
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        try:
            user.save(using=self._db)
            return user
        except Exception:
            raise ValueError('Duplicate email')

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True, blank=True)
    vkid = models.IntegerField('vk id', unique=True, blank=False, primary_key=True)
    first_name = models.CharField('first name', max_length=30, blank=True)  # WHY blank=True used?
    last_name = models.CharField('last name', max_length=30, blank=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('staff status', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name


class DialogManager():
    def create_dialog(self, user_vk_id):
        # Найти пользователя , собрать дефолтные задачи, выставить стэйт
        try:
            user = User.objects.get(pk=user_vk_id)
            dialog = self.create(user_vk_id=user_vk_id, state='NEED_NEXT_BOT_STATE')
            return dialog
        except Exception: # TODO посмотреть исключения
            raise ValueError('User with id {} not found'.format(user_vk_id))


class Dialog(models.Model):
    user_vk_id = models.IntegerField('vk id', unique=True, blank=False, primary_key=True)

    objects = DialogManager()

    STATES = (
        ('DEFAULT_BOT_STATE', 'Wait for any command'),
        ('NEED_NEXT_BOT_STATE', 'Wait for answer the question "Need the next block?"')
        ('WAIT_ANSWER_BOT_STATE', 'Wait for current block answer')
    )

    state = models.CharField(choices=STATES)

    blocks_ids = ArrayField(
        models.IntegerField(),
        verbose_name='Массив из id блоков',
        blank=True,
        default=[]
    )

    current_block_pointer = models.IntegerField('block pointer', default=0)

    @property
    def current_block_id(self):
        return self.current_block_pointer

    def update_pointer(self):
        """Перемещает указатель на следующую задачу в списке"""
        if current_block_pointer < blocks_ids.count() - 1:
            current_block_pointer += 1
