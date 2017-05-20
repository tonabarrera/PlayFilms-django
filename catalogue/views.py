from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from catalogue.models import Content, Episode


def content_list(request):
    content = Content.objects.all()
    for dato in content:
        print(dato.title)
    return render(request, 'catalogo.html', {'content': content})


def film_detail(request, pk):
    film = Content.objects.get(pk=pk)
    return render(request, 'pelicula.html', {'film': film})


def serie_detail(request, pk):
    serie = Content.objects.get(pk=pk)
    return render(request, 'serie.html', {'serie': serie})


def episode_detail(request, pk):
    episode = Episode.objects.get(pk=pk)
    return render(request, 'episode.html', {'episode': episode})
