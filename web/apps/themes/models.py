from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.blocks.models import Block
from apps.results.models import BlockResult
from apps.lessons.models import Lesson


class Theme(models.Model):
    # TODO: думаю, это лишнее, ибо мы оставляем темы и блоки без жесткой связи с уроками
    lesson = models.ForeignKey(
        Lesson,
        verbose_name='Урок',
        on_delete=models.CASCADE)

    title = models.CharField(
        verbose_name="Заголовок",
        max_length=60,
        blank=False
    )

    block_ids = ArrayField(
        models.IntegerField(),
        verbose_name='Массив из id блоков',
        blank=True
    )

    description = models.TextField(
        verbose_name="Описание",
        blank=False
    )
