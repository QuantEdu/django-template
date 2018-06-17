# Django core
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
# External libraries
from model_utils.managers import InheritanceManager


# Main model for all results
class Result(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=u'Ученик',
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)
    max_score = models.IntegerField(default=0)

    # From django-model-utils
    objects = InheritanceManager()

    class Meta:
        verbose_name = 'результат'
        verbose_name_plural = 'результаты'

    def correct(self):
        return self.score == self.max_score


# =================
# Results of blocks
# =================
class BlockResult(Result):
    block = models.ForeignKey('blocks.Block', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'результат ответа на блок'
        verbose_name_plural = 'результаты ответов на блоки'

    def __str__(self):
        return u'{}, {}, {}'.format(self.user, self.block, self.date)

    def block_subclass(self):
        return self.block.get_subclass()


class TextBlockResult(BlockResult):
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'результат: текст'
        verbose_name_plural = 'результаты: тексты'

    def set_score(self, new_score=0):
        # Загружаем и сохраняем текущую стоимость задания
        # Это не избыточно, так как max_score у Block может поменяться
        self.max_score = self.block.max_score
        if new_score:
            if new_score <= self.max_score:
                self.score = new_score
            else:
                self.score = self.max_score
        # при назначенном флаге is_read автоматически выставит оценку
        else:
            if self.is_read:
                self.score = self.max_score
            else:
                self.score = 0
        self.save()


class ChoiceBlockResult(BlockResult):
    # ссылки на id СhoiсeBlockOptions
    answers = ArrayField(models.IntegerField())

    class Meta:
        verbose_name = 'результат: выбор'
        verbose_name_plural = 'результаты: выбор'

    # Get user answer and true answer
    def get_answer(self):
        choice_block = self.block.get_subclass()

        return choice_block.get_options_by_pks(self.answers)[::1], choice_block.get_true_options()[::1]

    def set_score(self, new_score=0):
        # Загружаем и сохраняем текущую стоимость задания
        # Это не избыточно, так как max_score у Block может поменяться
        self.max_score = self.block.max_score
        if new_score:
            if new_score <= self.max_score:
                self.score = new_score
            else:
                self.score = self.max_score
        # вычисляет балл на основе количества ответов (по 1 на каждый верный)
        else:
            self.max_score = 0
            self.score = 0

            import apps.blocks
            choices = apps.blocks.models.ChoiceBlockOption.objects.filter(choice_block=self.block)
            answers_list_of_int = list(map(int, self.answers))
            for choice in choices:
                if choice.is_true:
                    self.max_score += 1
                    if choice.id in answers_list_of_int:
                        self.score += 1
        self.save()


class FloatBlockResult(BlockResult):
    answer = models.FloatField('Ответ', null=True, default=None)

    class Meta:
        verbose_name = 'результат: числовой ответ'
        verbose_name_plural = 'результаты: числовой ответ'

    # Get user answer and true answer
    def get_answer(self):
        return self.answer, self.block.get_subclass().true_answer

    def set_score(self, new_score=0):
        # Загружаем и сохраняем текущую стоимость задания
        # Это не избыточно, так как max_score у Block может поменяться
        self.max_score = self.block.max_score
        if new_score:
            if new_score <= self.max_score:
                self.score = new_score
            else:
                self.score = self.max_score
        else:
            if self.answer is None or self.answer == "":
                self.score = 0
            elif float(self.answer) == self.block.true_answer:
                self.score = self.max_score
            else:
                self.score = 0
        self.save()


class TextAnswerBlockResult(BlockResult):
    answer = models.CharField(max_length=100, null=True)  # ответ, который дал ученик

    class Meta:
        verbose_name = 'результат: текстовый ответ'
        verbose_name_plural = 'результаты: текстовый ответ'

    # Get user answer and true answer
    def get_answer(self):
        return self.answer, self.block.get_subclass().true_answer

    def set_score(self, new_score=0):
        # Загружаем и сохраняем текущую стоимость задания
        # Это не избыточно, так как max_score у Block может поменяться
        self.max_score = self.block.max_score

        if new_score:
            if new_score <= self.max_score:
                self.score = new_score
            else:
                self.score = self.max_score
        else:
            if self.answer == self.block.true_answer:
                self.score = self.max_score
            else:
                self.score = 0
        self.save()
