"""timelog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import log.urls as log_urls

from log.api import LogResource
from company.api import UserResource
from tastypie.api import Api

api = Api(api_name='api')

api.register(LogResource())
api.register(UserResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(log_urls)),
    url(r'', include(api.urls)),
]
