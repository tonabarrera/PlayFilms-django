from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from PlayFilms import settings
from catalogue.models import Content, Episode

# Create your views here.
from userprofiles.models import History


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


def buscar(request):
    content = None
    name = None

    if request.method == 'GET':
        name = request.GET.get('q', None)
        if name is not None:
            print(name)
            content = Content.objects.filter(title__contains=name)
    if name is None:
        content = Content.objects.all()
    return content


@login_required(login_url='/user/login/')
def content_list(request):
    print(settings.STATIC_ROOT)
    data = cargar_info_usuario(request)
    content = buscar(request)
    return render(request, 'catalogo.html', {'catalogue': content, 'data': data})


@login_required(login_url='/user/login/')
def film_detail(request, pk):
    film = Content.objects.get(pk=pk)
    data = cargar_info_usuario(request)
    temp_user = request.user.userprofile
    if History.objects.filter(user_profile=temp_user, content=film, is_favorite=True).exists():
        data['fav_submit'] = 'Quitar de favoritos'
    else:
        data['fav_submit'] = 'Agregar a favoritos'

    return render(request, 'pelicula.html', {'film': film, 'data': data})


@login_required(login_url='/user/login/')
def serie_detail(request, pk):
    serie = Content.objects.get(pk=pk)
    data = cargar_info_usuario(request)
    temp_user = request.user.userprofile
    if History.objects.filter(user_profile=temp_user, content=serie, is_favorite=True).exists():
        data['fav_submit'] = 'Quitar de favoritos'
    else:
        data['fav_submit'] = 'Agregar a favoritos'
    return render(request, 'serie.html', {'serie': serie, 'data': data})


@login_required(login_url='/user/login/')
def episode_detail(request, pk):
    episode = Episode.objects.get(pk=pk)
    data = cargar_info_usuario(request)
    return render(request, 'episode.html', {'episode': episode, 'data': data})

def agregar_favorito_view(request):
    data = {'error': 'error'}
    if request.method == 'GET':
        pk = int(request.GET.get('film', None))
        if pk is not None:
            film = Content.objects.get(id=pk)
            temp_user = request.user.userprofile
            if temp_user.favorites.filter(id=pk).exists():
                history = History.objects.get(user_profile=temp_user, content=film)
                history.is_favorite = not history.is_favorite
                data = {'favorito': history.is_favorite}
                history.save()
            else:
                data = {'favorito': True}
                history = History.objects.create(user_profile=temp_user, content=film, is_favorite=True)
                history.save()
    return JsonResponse(data)


def puntuar_view(request):
    data = {'ok': False}
    if request.method == 'GET':
        pk = int(request.GET.get('film', None))
        score = int(request.GET.get('calificacion', None))
        if (pk and score) is not None:
            film = Content.objects.get(id=pk)
            temp_user = request.user.userprofile
            if temp_user.favorites.filter(id=pk).exists():
                history = History.objects.get(user_profile=temp_user, content=film)
                history.score = score
                history.save()
            else:
                history = History.objects.create(user_profile=temp_user, content=film, score=score)
                history.save()
            data['puntaje'] = Content.objects.get(id=pk).score
            data['ok'] = True
    return JsonResponse(data)
