from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from catalogue.models import Content, Episode


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


@login_required(login_url='/user/login/')
def content_list(request):
    content = Content.objects.all()
    data = cargar_info_usuario(request)
    return render(request, 'catalogo.html', {'content': content, 'data': data})


@login_required(login_url='/user/login/')
def film_detail(request, pk):
    film = Content.objects.get(pk=pk)
    data = cargar_info_usuario(request)
    return render(request, 'pelicula.html', {'film': film, 'data': data})


@login_required(login_url='/user/login/')
def serie_detail(request, pk):
    serie = Content.objects.get(pk=pk)
    data = cargar_info_usuario(request)
    return render(request, 'serie.html', {'serie': serie, 'data': data})


@login_required(login_url='/user/login/')
def episode_detail(request, pk):
    episode = Episode.objects.get(pk=pk)
    data = cargar_info_usuario(request)
    return render(request, 'episode.html', {'episode': episode, 'data': data})
