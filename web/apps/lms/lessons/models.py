from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.studio.tags import SubjectTag


class Lesson(models.Model):
    subject = models.ForeignKey(
        SubjectTag,
        verbose_name='Предмет',
        on_delete=models.CASCADE)

    title = models.CharField(
        verbose_name="Заголовок",
        max_length=60,
        blank=False
    )

    themes_ids = ArrayField(
        models.IntegerField(),
        verbose_name='Массив из id тем',
        blank=True
    )

    description = models.TextField(
        verbose_name="Описание",
        blank=False
    )
