# Django core
from django.db import models


# Vk authorization
class VKAuth(models.Model):
    # user = models.
    uid = models.CharField( verbose_name="Заголовок", max_length=60, blank=False)
    photo = models.CharField(verbose_name="Заголовок", max_length=60, blank=False)
    hash = models.CharField(verbose_name="Заголовок", max_length=60, blank=False)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)

    class Meta:
        verbose_name = 'Авторизация в VK'
        verbose_name_plural = 'Авторизации в VK'

    def __str__(self):
        return self.uid
