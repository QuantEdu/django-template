from django.db import models
from django.utils import timezone

from crm.users.models import User
from lms.lessons.models import Lesson

# Main model for tasks
class Task(models.Model):

    lesson = models.ForeignKey(Lesson, verbose_name="Урок", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    deadline = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'задание по уроку'
        verbose_name_plural = 'задания по уроку'

    def __str__(self):
        return u'{}, {}'.format(self.user, self.lesson)


