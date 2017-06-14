from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
# Create your models here.
from django.db.models import Avg

from catalogue.models import Content


def get_upload_path(instance, filename):
    return 'avatars/user_{0}/{1}'.format(instance.user.id, filename)


class UserProfile(models.Model):
    type_of_user_choices = (
        (1, 'Premium'),
        (2, 'Estandar')
    )
    user = models.OneToOneField(User)
    type_of_user = models.IntegerField(choices=type_of_user_choices, default=2, verbose_name='tipo de usuario')
    avatar = models.ImageField(upload_to=get_upload_path, blank=True, default='avatars/default_app_avatar.png', max_length=250)
    favorites = models.ManyToManyField(Content, through='History')

    class Meta:
        verbose_name = 'Perfil de usuario'
        verbose_name_plural = 'Perfiles de usuario'

    def email(self):
        return self.user.email

    def __str__(self):
        return self.user.username


class History(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='perfil de usuario')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name='contenido')
    score = models.PositiveIntegerField(blank=True, default=5, verbose_name='puntuación')
    is_favorite = models.BooleanField(default=False, verbose_name='es favorito')

    class Meta:
        verbose_name = verbose_name_plural = 'Historial'

    def save(self, *args, **kwargs):
        super(History, self).save(*args, **kwargs)
        c = self.content
        c.score = round(c.history_set.aggregate(Avg('score'))['score__avg'], 1)
        c.save()


class CreditCard(models.Model):
    MONTH_CHOICES = (
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
        ('07', '07'),
        ('08', '08'),
        ('09', '09'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )
    YEAR_CHOICES = []
    for n in range(17, 45):
        YEAR_CHOICES.append((str(n), str(n)))
    number = models.CharField(max_length=19, validators=[RegexValidator(r'^\d{1,19}$')], unique=True,
                              verbose_name='Numero de tarjeta')
    owner = models.CharField(max_length=45, verbose_name='Dueño', blank=True)
    due_month = models.CharField(max_length=2, choices=MONTH_CHOICES, verbose_name='Mes')
    due_year = models.CharField(max_length=2, choices=YEAR_CHOICES, verbose_name='Año')
    CVV = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,10}$')])
    user_profile = models.OneToOneField(UserProfile, verbose_name='perfil de usuario')

    class Meta:
        verbose_name = 'tarjeta de credito'
        verbose_name_plural = 'Tarjetas de credito'

    def __str__(self):
        return self.user_profile.user.username + ': ' + self.number
