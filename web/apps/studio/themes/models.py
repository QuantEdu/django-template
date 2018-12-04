from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.studio.blocks.models import Block
from apps.lms.results.models import BlockResult
from apps.lms.lessons.models import Lesson


class Theme(models.Model):
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
