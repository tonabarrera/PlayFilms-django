from django.db import models


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=255, verbose_name='nombre')
    rol = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = 'actores'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='genero')

    class Meta:
        verbose_name_plural = 'generos'
        verbose_name = 'genero'

    def __str__(self):
        return self.name


class Content(models.Model):
    type_of_content_choices = (
        (1, "Pelicula"),
        (2, "Serie")
    )
    title = models.CharField(max_length=100, verbose_name='Titulo')
    content_file = models.FileField(upload_to='content', blank=True, verbose_name='archivo de video')
    score = models.FloatField(default=5, verbose_name='puntuación')
    actors = models.ManyToManyField(Actor, blank=True, verbose_name='actores')
    type_of_content = models.IntegerField(choices=type_of_content_choices, verbose_name='Tipo de contenido')
    genre = models.ForeignKey(Genre, verbose_name='Genero')
    cover = models.ImageField(upload_to='covers', blank=True, verbose_name='Portada')
    description = models.CharField(max_length=250, verbose_name='Descripcion')

    class Meta():
        ordering = ['title', 'score']
        verbose_name = verbose_name_plural = 'contenido'

    def __str__(self):
        return self.title

    def player(self):
        return """
        <video controls width="200">
          <source src="%s" type="video/mp4">
        Your browser does not support the video element.
        </video>""" % self.content_file.url

    player.allow_tags = True


class Episode(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    order = models.PositiveIntegerField(verbose_name='Orden')
    episode_file = models.FileField(upload_to='content', verbose_name='Archivo del episodio')
    serie = models.ForeignKey(Content, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Episodio'
        verbose_name_plural = 'Episodios'
    def __str__(self):
        return self.title
