from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie import fields

from models import Log


class LogResource(ModelResource):

    class Meta:
        queryset = Log.objects.all()
        resource_name = 'log'
        filtering = {
            "name": ALL_WITH_RELATIONS
        }
