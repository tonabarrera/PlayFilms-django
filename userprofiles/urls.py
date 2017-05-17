from django.conf.urls import url
from django.views.generic import RedirectView
from userprofiles.views import LoginView, LoginRedirectView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'', LoginRedirectView.as_view())
]