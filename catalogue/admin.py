from django.contrib import admin

# Register your models here.
from catalogue.models import Content, Actor, Genre, Episode


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'score', 'type_of_content', 'genre', 'description',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'rol',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'serie',)
