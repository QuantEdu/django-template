from django.contrib.postgres.fields import ArrayField
from django.db import models

from studio.blocks.models import Block
from lms.results.models import BlockResult
from lms.lessons.models import Lesson


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
