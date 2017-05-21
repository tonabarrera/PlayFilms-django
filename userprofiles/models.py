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
    favorites = models.ManyToManyField(Content, through='History')

    def email(self):
        return self.user.email
    def __str__(self):
        return self.user.username


class History(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(blank=True, default=5)
    is_favorite = models.BooleanField(default=False)

class CreditCard(models.Model):
    number = models.CharField(max_length=19, validators=[RegexValidator(r'^\d{1,10}$')])
    owner = models.CharField(max_length=45)
    due_date = models.DateField()
    cvv = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,10}$')])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
