# Django core
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Our apps
from apps.tags.models import GradeTag, SubjectTag


# Услуга, например курс, телеграм-эстафета итд...
class Service(models.Model):
    title = models.CharField(
        verbose_name='Название сервиса',
        max_length=300
    )

    class Meta:
        verbose_name = 'сервис'
        verbose_name_plural = 'сервисы'

    def __str__(self):
        return self.title


# Телеграм-курс
class TelegramService(Service):
    class_tag = models.ForeignKey(
        GradeTag,
        verbose_name='Класс',
        on_delete=models.CASCADE
    )
    subject_tag = models.ForeignKey(
        SubjectTag,
        verbose_name='Предмет',
        related_name='subject_tag',
        on_delete=models.CASCADE
    )
    # array of block's ids
    blocks_ids = ArrayField(
        models.IntegerField(),
        verbose_name='Массив из id блоков',
        blank=True
    )

    class Meta:
        verbose_name = 'телеграм-курс'
        verbose_name_plural = 'телеграм-курсы'

    def __str__(self):
        return u'{} {}'.format(self.class_tag, self.subject_tag)


# Связь услуги и пользователя для управления подписками
class StudentServiceRelation(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'связь сервиса со студентом'
        verbose_name_plural = 'связи сервисов со студентами'

    def __str__(self):
        return u'{} {}'.format(self.student, self.service)
