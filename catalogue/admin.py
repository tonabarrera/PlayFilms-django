from django.contrib import admin

# Register your models here.
from catalogue.models import Content, Actor, Category, Episode


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'score', 'type_of_content', 'category',)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'serie',)
