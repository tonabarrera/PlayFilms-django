from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import FormView, RedirectView, ListView

from catalogue.models import Content


class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/catalogo/'

    def dispatch(self, request, *args, **kwargs):
        print('En dispatch')
        if request.user.is_authenticated():
            print('Aqui')
            return HttpResponseRedirect('/catalogo/')
        else:
            print('No deberia estar aqui')
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('/user/login')
