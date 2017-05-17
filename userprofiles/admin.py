from django.contrib import admin

# Register your models here.
from userprofiles.models import UserProfile, UserContent, UserFavorites, UserCard


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'type_of_user')


@admin.register(UserContent)
class UserTrackAdmin(admin.ModelAdmin):
    pass


@admin.register(UserFavorites)
class UserFavoriteAdmin(admin.ModelAdmin):
    pass


@admin.register(UserCard)
class UserCardAdmin(admin.ModelAdmin):
    pass
