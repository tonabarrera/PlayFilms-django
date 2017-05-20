from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
from django.views.generic import FormView, RedirectView, ListView

from catalogue.models import Content