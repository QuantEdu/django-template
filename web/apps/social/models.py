# Django core
from django.db import models
from django.contrib.postgres.fields import JSONField

# Our apps
from apps.users.models import User


class UserSocialAuth(models.Model):
    user = models.ForeignKey(
        User,
        related_name='social_auth',
        on_delete=models.CASCADE
    )
    provider = models.CharField(max_length=32)
    uid = models.CharField(verbose_name="Uid", max_length=60, blank=False)
    extra_data = JSONField()

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Авторизация в соцсетях'
        verbose_name_plural = 'Авторизации в соцсетях'

    # Вернет пользователя, если он существует
    def get_social_auth(self, provider, uid):
        try:
            return self.objects.select_related('user').get(provider=provider, uid=uid)
        except self.DoesNotExist:
            return None

    # def allowed_to_disconnect
