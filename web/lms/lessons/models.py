from django.contrib.postgres.fields import ArrayField
from django.db import models

from studio.tags.models import SubjectTag


class Lesson(models.Model):
    # group
    # classroom
    # auditory
    # datetime
    # duration
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


class UserLesson(models.Model):
    mark = models.IntegerField()
    # group
    # lesson
    # visit_status
