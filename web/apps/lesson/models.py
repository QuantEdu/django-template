from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.blocks.models import Block
from apps.results.models import BlockResult
from apps.course.models import Course

class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        verbose_name='Курс',
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
