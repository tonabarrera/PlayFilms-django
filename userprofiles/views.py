from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import FormView, RedirectView, ListView

from catalogue.models import Content

def cargar_info_usuario(request):
    is_auth = False
    username = None
    if request.user.is_authenticated():
        is_auth = True
        username = request.user.username
    data = {
        'is_auth': is_auth,
        'username': username,
    }
    return data

class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/catalogo/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/catalogo/')
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('/user/login')


class LoginRedirectView(RedirectView):
    permanent = True
    pattern_name = 'user:login'

class FavoritesListView(LoginRequiredMixin, ListView):
    model = Content
    template_name = 'catalogo.html'
    context_object_name = 'catalogue'
    login_url = '/user/login'

    def get_queryset(self):
        queryset = self.model.objects.filter(userprofile__user=self.request.user, history__is_favorite=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FavoritesListView, self).get_context_data(**kwargs)
        data = cargar_info_usuario(self.request)
        context['data'] = data
        return context

