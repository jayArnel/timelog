from __future__ import unicode_literals
from django.utils import timezone

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


class Employee(models.Model):

    user = models.OneToOneField(User, related_name='employee')
    company = models.ForeignKey(Company, related_name='employees')

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.user.get_full_name()

    @property
    def is_timed_in(self):
        last_log = self.user.logs.all().last()
        return last_log and not last_log.end

    def timeout(self):
        last_log = self.user.logs.all().last()
        last_log.end = timezone.now()
        last_log.save()
