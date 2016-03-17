import json

from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.views.generic import TemplateView, View
# Create your views here.


class HomeView(TemplateView):
    template_name = 'log/home/home.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            msg = {}
            if user is not None:
                if user.is_active:
                    login(request, user)
                    msg['status'] = 401
                    msg['redirect_url'] = '/log'
                else:
                    msg['error'] = "This user account is deactivated. \
                        Please contact your administrator"
                    msg['status'] = 401
            else:
                msg['error'] = "Invalid username/password combination"
                msg['status'] = 401
            return HttpResponse(json.dumps(msg))
        return HttpResponseForbidden()


class LogView(TemplateView):
    template_name = 'log/timelog/timelog.html'
