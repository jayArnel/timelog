from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Log(models.Model):

    owner = models.ForeignKey(User, related_name='logs')
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"

    def __str__(self):
        return '{0}\'s log at {1}'.format(self.owner.first_name, self.start)
