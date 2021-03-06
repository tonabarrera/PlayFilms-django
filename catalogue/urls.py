from django.conf.urls import url

from catalogue import views
from catalogue.views import GenreListView, ContentListView

urlpatterns = [
    url(r'^$', ContentListView.as_view(), name='content'),
    #url(r'^(?P<name>[\w\-]+)/$', ContentListView.as_view(), name='content_search'),
    url(r'^pelicula/(?P<pk>[0-9]+)/$', views.film_detail, name='pelicula'),
    url(r'^serie/(?P<pk>[0-9]+)/$', views.serie_detail, name='serie'),
    url(r'^episode/(?P<pk>[0-9]+)/$', views.episode_detail, name='episode'),
    url(r'^agregar/$', views.agregar_favorito_view, name='agregar'),
    url(r'^puntuar/$', views.puntuar_view, name='puntuar'),
    url(r'^peliculas/$', views.movies_view, name='movies'),
    url(r'^series/$', views.series_view, name='series'),
    url(r'^generos/(?P<genre>[\w\-\s]+)/$', GenreListView.as_view(), name='generos'),
    url(r'^busqueda/', views.content_list, name='buscar'),
]