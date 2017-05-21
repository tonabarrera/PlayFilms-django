from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from userprofiles.models import UserProfile, History, UserCard


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'type_of_user')


@admin.register(History)
class UserHistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(UserCard)
class UserCardAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(Group)