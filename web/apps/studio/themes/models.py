from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.studio.blocks import Block
from apps.lms.results import BlockResult
from apps.lms.lessons.models import Lesson


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
