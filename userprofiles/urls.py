from django.conf.urls import url

from userprofiles import views
from userprofiles.views import LoginView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),

]
