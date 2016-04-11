from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = [
            'email', 'password', 'is_active', 'is_staff', 'is_superuser']
        filtering = {
            'pk': ALL,
        }
