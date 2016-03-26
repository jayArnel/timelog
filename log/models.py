from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import localtime
# Create your models here.


class Log(models.Model):

    owner = models.ForeignKey(User, related_name='logs')
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"

    def __str__(self):
        name = (self.owner.username
                if self.owner.first_name == '' else self.owner.first_name)
        start = localtime(self.start).strftime('%B %d, %Y %I:%M%p')
        return '{0}\'s log on {1}'.format(name, start)
