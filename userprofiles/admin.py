from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from userprofiles.models import UserProfile, History, CreditCard


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'type_of_user')


@admin.register(History)
class UserHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'is_favorite', 'score')

@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(Group)