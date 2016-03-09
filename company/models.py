from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Company(models.Model):

    name = models.CharField(max_length=40)
    admin = models.OneToOneField(User, related_name='company')

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name
