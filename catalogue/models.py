from django.db import models


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=255)
    rol = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Content(models.Model):
    type_of_content_choices = (
        (1, "Pelicula"),
        (2, "Serie")
    )
    title = models.CharField(max_length=100)
    content_file = models.FileField(upload_to='content', blank=True)
    score = models.FloatField(default=5)
    actors = models.ManyToManyField(Actor, blank=True)
    type_of_content = models.IntegerField(choices=type_of_content_choices)
    category = models.ForeignKey(Category)
    cover = models.ImageField(upload_to='covers', blank=True)

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
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField()
    episode_file = models.FileField(upload_to='content')
    serie = models.ForeignKey(Content)

    def __str__(self):
        return self.title