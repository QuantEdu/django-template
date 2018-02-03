# Django core
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# External libraries
from polymorphic.models import PolymorphicModel

# Our apps
from apps.blocks import Block, ChoiceBlockOption


# Main model for all results
class Result(PolymorphicModel):
    student = models.ForeignKey(User, verbose_name=u'Ученик')
    date = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)
    max_score = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'результат'
        verbose_name_plural = 'результаты'


# =================
# Results of blocks
# =================
class BlockResult(Result):
    block = models.ForeignKey(Block)

    class Meta:
        verbose_name = 'результат ответа на блок'
        verbose_name_plural = 'результаты ответов на блоки'

    def __str__(self):
        return u'{}, {}, {}'.format(self.student, self.block, self.date)

    # Вызывается в момент получения решения от ученика
    def set_score(self, cur_score=0):
        # Загружаем и сохраняем текущую стоимость задания.
        # Это не избыточно, так как max_score у Block может поменяться
        self.max_score = self.block.score
        if cur_score:
            if cur_score <= self.max_score:
                self.score = cur_score


class TextBlockResult(BlockResult):
    answer = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'результат изучения текстового блока'
        verbose_name_plural = 'результаты изучения текстовых блоков'

    def set_score(self, cur_score=0):
        self.max_score = self.block.score
        if cur_score:
            if cur_score <= self.max_score:
                self.score = cur_score
        else:
            if self.answer:
                self.score = self.max_score
        self.save()

class ChoiceBlockResult(BlockResult):
    answer = ArrayField(models.IntegerField()) # ссылки на id choiseBlockOptions

    class Meta:
        verbose_name = 'результат ответа на тестовый вопрос'
        verbose_name_plural = 'результаты ответов на тестовые вопросы'

    def set_score(self, cur_score=0):
        choices = ChoiceBlockOption.objects.filter(choice_block=self.block)
        self.max_score = 0
        self.score = 0
        if cur_score:
            if cur_score <= self.max_score:
                self.score = cur_score
        else:
            for ch in choices:
                if ch.is_true:
                    self.max_score += 1
                    if ch.id in self.answer:
                        self.score += 1
        self.save()

class FloatBlockResult(BlockResult):
    answer = models.FloatField('Ответ', null=True, default=None)

    class Meta:
        verbose_name = 'результат ответа на задачу'
        verbose_name_plural = 'результаты ответов на задачи'

    def set_score(self, cur_score=0):
        self.max_score = self.block.score
        correct_answer = self.block.answer
        if cur_score:
            if cur_score <= self.max_score:
                self.score = cur_score
        else:
            if self.answer is None or self.answer == "":
                self.score = 0
            elif float(self.answer) == correct_answer:
                self.score = self.max_score
        self.save()

class TextAnswerBlockResult(BlockResult):
    answer = models.CharField(max_length=100, null=True) # ответ, который дал ученик

    class Meta:
        verbose_name = 'результат ответа на задание с текстовым ответом'
        verbose_name_plural = 'результаты ответов на задание с текстовым ответом'

    def set_score(self, cur_score=0):
        self.max_score = self.block.score
        correct_answer = self.block.answer
        if cur_score:
            if cur_score <= self.max_score:
                self.score = cur_score
        else:
            if self.answer == correct_answer:
                self.score = self.max_score
        self.save()

# ========================
# Relation between results
# ========================
class TaskResultBlockResultRelation(models.Model):
    task_result = models.ForeignKey(TaskResult)
    block_result = models.ForeignKey(BlockResult)

    class Meta:
        verbose_name = 'связь результата задания с результатом блока'