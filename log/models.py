from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
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
        start = timezone.localtime(self.start).strftime('%B %d, %Y %I:%M%p')
        return '{0}\'s log on {1}'.format(name, start)

    @property
    def display(self):
        now = timezone.localtime(timezone.now())
        start = timezone.localtime(self.start)
        diff = now - start
        prefix = ''
        if diff.days < 1:
            prefix = 'Today'
        elif diff.days >= 1 and diff.days < 2:
            prefix = 'Yesterday'
        elif diff.days >= 2 and now.year > start.year:
            prefix = start.strftime('%B %d, %Y')
        return {'prefix': prefix, 'time': start.strftime('%I:%M%p')}
