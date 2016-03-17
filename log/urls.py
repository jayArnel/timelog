from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^log/$', views.LogView.as_view(), name='log'),
    url(r'^timein/$', views.TimeInView.as_view(), name='timein'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]
