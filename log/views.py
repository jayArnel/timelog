import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.conf import settings
from django.http import (
    HttpResponse, HttpResponseForbidden, HttpResponseRedirect)
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, View
# Create your views here.

from log.models import Log
from company.models import Employee


class HomeView(TemplateView):
    template_name = 'log/home/home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        return super(HomeView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            msg = {}
            if user is not None:
                if user.is_active:
                    login(request, user)
                    msg['status'] = 200
                    msg['redirect_url'] = settings.LOGIN_REDIRECT_URL
                else:
                    msg['error'] = "This user account is deactivated. \
                        Please contact your administrator"
                    msg['status'] = 401
            else:
                msg['error'] = "Invalid username/password combination"
                msg['status'] = 401
            return HttpResponse(json.dumps(msg))
        return HttpResponseForbidden()


class LogoutView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class LogView(LoginRequiredMixin, TemplateView):
    template_name = 'log/timelog/timelog.html'

    def get_context_data(self, **kwargs):
        context = {}
        employee = Employee.objects.get(user__pk=self.request.user.pk)
        context['employee'] = employee
        return context


class TimeInView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        status = 400
        if request.is_ajax():
            pk = request.POST.get('pk')
            user = get_object_or_404(User, pk=pk)
            if request.user == user:
                status = 200
                Log.objects.create(owner=user)
            else:
                status = 401
        return HttpResponse(status=status)
