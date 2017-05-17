from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from catalogue.models import Content


class UserProfile(models.Model):
    type_of_user_choices = (
        (1, 'Premium'),
        (2, 'Estandar')
    )
    user = models.OneToOneField(User)
    type_of_user = models.IntegerField(choices=type_of_user_choices)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    favorites = models.ManyToManyField()


class UserContent(models.Model):
    user = models.ForeignKey(User)
    content = models.ForeignKey(Content)
    score = models.PositiveIntegerField()


class UserFavorites(models.Model):
    user = models.ForeignKey(User)
    content = models.ForeignKey(Content)


class UserCard(models.Model):
    number = models.PositiveIntegerField()
    owner = models.CharField(max_length=45)
    due_date = models.DateField()
    cvv = models.PositiveIntegerField()
    user = models.ForeignKey(User)
