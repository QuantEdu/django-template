# Django core
from django.db import models
# External libraries
from model_utils.managers import InheritanceManager


# All blocks, results etc can be tagged
# For example we provide:
#    - Subject Tag (физика, математика итд)
#       - Exam Tag (задача №13 из егэ по математике - указать тип экзамена и номер)
class Tag(models.Model):

    # From django-model-utils
    objects = InheritanceManager()

    def __str__(self):
        return u'Tag #{}'.format(self.id)

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


# Grade model
# FIXME: maybe should be in separate app
class Grade(models.Model):
    grade_num = models.SmallIntegerField(
        verbose_name='Номер класса')

    class Meta:
        verbose_name = 'номер класса'
        verbose_name_plural = 'номера классов'

    def __str__(self):
        return u'{} класс'.format(self.grade_num)


# Pointer to grade: 9, 10, 11 etc
class GradeTag(Tag):
    grade = models.ForeignKey(
        Grade,
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'тег-указатель на класс'
        verbose_name_plural = 'теги-указательи на классы'

    def __str__(self):
        return str(self.grade)


# Subject model for dynamically creation
# FIXME: maybe should be in separate app
class Subject(models.Model):
    title = models.CharField(
        verbose_name='Название предмета',
        max_length=300)

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'

    def __str__(self):
        return self.title


# Pointer to subject
class SubjectTag(Tag):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'тег-указатель на предмет'
        verbose_name_plural = 'теги-указатели на предметы'

    def __str__(self):
        return self.subject.title


# Pointer to position in exam. can be used for quizzes creating
class ExamTag(SubjectTag):

    EXAM_TYPES = (
        ('EGE', 'ЕГЭ'),
        ('OGE', 'ОГЭ'),
    )

    exam_type = models.CharField(
        verbose_name='Тип экзамена',
        max_length=5,
        choices=EXAM_TYPES,
        default='EGE')
    order = models.SmallIntegerField(
        verbose_name='Порядковый номер в экзамене',
        help_text='Если есть',
        null=True,
        blank=True)
    exam_year = models.PositiveSmallIntegerField(
        verbose_name='Год проведения экзамена',
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'тег-указатель на положение в экзамене'
        verbose_name_plural = 'теги-указатели на положение в экзамене'

    def __str__(self):
        return u'{} {} №{} ({})'.format(self.subject.title, self.get_exam_type_display(), self.order, self.exam_year)


# Pointer to service
class ServiceTag(Tag):
    service = models.ForeignKey(
        'services.Service',
        related_name='service_for_tag',
        max_length=300,
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'тег-указатель на сервис'
        verbose_name_plural = 'теги-указатели на сервисы'

    def __str__(self):
        return self.service.title
