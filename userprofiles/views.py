from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
from django.views.generic import FormView, RedirectView, ListView

from catalogue.models import Content


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = 'home'

    def form_valid(self, form):
        print('form_valid')
        login(self.request, form.user_cache)

        return super(LoginView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        is_auth = False
        name = None

        if self.request.user.is_authenticated():
            is_auth = True
            name = self.request.user.username

        data = {
            'is_auth': is_auth,
            'name': name,
        }

        context.update(data)
        return context

class LoginRedirectView(RedirectView):
    permanent = True
    pattern_name = 'login'