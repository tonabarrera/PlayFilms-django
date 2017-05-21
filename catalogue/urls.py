from django.conf.urls import url

from catalogue import views

urlpatterns = [
    url(r'^$', views.content_list, name='content'),
    #url(r'^(?P<name>[\w\-]+)/$', ContentListView.as_view(), name='content_search'),
    url(r'^pelicula/(?P<pk>[0-9]+)/$', views.film_detail, name='pelicula'),
    url(r'^serie/(?P<pk>[0-9]+)/$', views.serie_detail, name='serie'),
    url(r'^episode/(?P<pk>[0-9]+)/$', views.episode_detail, name='episode'),
    url(r'^agregar/$', views.agregar_favorito_view, name='agregar'),
    url(r'^puntuar/$', views.puntuar_view, name='puntuar'),
]