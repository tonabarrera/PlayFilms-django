from django.conf.urls import url
from django.views.generic import RedirectView

from catalogue.views import ContentListView
from userprofiles.views import LoginView, LoginRedirectView

urlpatterns = [
    url(r'^home/$', ContentListView.as_view(), name='home'),
]