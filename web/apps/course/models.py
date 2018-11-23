from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.tags.models import SubjectTag

class Course(models.Model):
    subject = models.ForeignKey(
        SubjectTag,
        verbose_name='Предмет',
        on_delete=models.CASCADE)

    title = models.CharField(
        verbose_name="Заголовок",
        max_length=60,
        blank=False
    )

    lesson_ids = ArrayField(
        models.IntegerField(),
        verbose_name='Массив из id уроков',
        blank=True
    )

    description = models.TextField(
        verbose_name="Описание",
        blank=False
    )