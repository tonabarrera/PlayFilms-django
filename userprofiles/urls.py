from django.conf.urls import url

from userprofiles import views
from userprofiles.views import LoginView, FavoritesListView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^favorites/$', FavoritesListView.as_view(), name='favorites'),
    url(r'^signup/$', views.signUp_view, name='signup'),
    url(r'^reset/$', views.reset_password_view, name='reset'),
    url(r'^profile/$', views.profile_view, name='profile'),
    url(r'borrar/$', views.borrar_view, name='borrar'),
]
