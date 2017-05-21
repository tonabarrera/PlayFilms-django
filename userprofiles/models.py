from django.contrib.auth.models import User
from django.core.validators import RegexValidator
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
    favorites = models.ManyToManyField(Content)

    def email(self):
        return self.user.email


class History(models.Model):
    user = models.ForeignKey(User)
    content = models.ForeignKey(Content)
    score = models.PositiveIntegerField(blank=True)


class UserCard(models.Model):
    number = models.CharField(max_length=19, validators=[RegexValidator(r'^\d{1,10}$')])
    owner = models.CharField(max_length=45)
    due_date = models.DateField()
    cvv = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,10}$')])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
