from datetime import datetime

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, EmailMultiAlternatives
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView, RedirectView, ListView

from PlayFilms.mixins import PremiumRequiredMixin
from catalogue.models import Content
from userprofiles.forms import UserForm, UserProfileForm, CreditCardForm


def cargar_info_usuario(request):
    is_auth = False
    username = None
    if request.user.is_authenticated():
        is_auth = True
        username = request.user.username
    data = {
        'is_auth': is_auth,
        'username': username,
    }
    return data


# actualizar los datos de la tarjeta
class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/catalogo/'

    def dispatch(self, request, *args, **kwargs):
        print('dispatch')
        if request.user.is_authenticated():
            return HttpResponseRedirect('/catalogo/')
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        print('login')
        user = form.get_user()
        profile = user.userprofile
        card = profile.creditcard
        validar_tarjeta(card, profile)
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


def validar_tarjeta(card, profile):
    card_year = int(card.due_year) + 2000
    card_month = int(card.due_month)
    card_date = datetime(card_year, card_month, 1)
    current_date = datetime.now()
    current_date = current_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    if card_date >= current_date:
        profile.type_of_user = 1
    else:
        profile.type_of_user = 2
    profile.save()


def signUp_view(request):
    if request.method == 'POST':
        uform = UserForm(request.POST)
        pform = UserProfileForm(request.POST, request.FILES)
        cform = CreditCardForm(request.POST)
        if uform.is_valid() and pform.is_valid() and cform.is_valid():
            user = uform.save()
            profile = pform.save(commit=False)
            card = cform.save(commit=False)
            profile.user = user
            profile.avatar = pform.cleaned_data['avatar']
            profile.save()
            card.user_profile = profile
            card.save()
            validar_tarjeta(card, profile)
            print('Se registro')
            login(request, user)
            return redirect('/catalogo/')
    else:
        uform = UserForm()
        pform = UserProfileForm()
        cform = CreditCardForm()
    return render(request, 'signup.html', {'uform': uform, 'pform': pform, 'cform': cform})


def logout_view(request):
    logout(request)
    return redirect('/user/login')


class LoginRedirectView(RedirectView):
    permanent = True
    pattern_name = 'user:login'


class FavoritesListView(PremiumRequiredMixin, LoginRequiredMixin, ListView):
    model = Content
    template_name = 'catalogo.html'
    context_object_name = 'catalogue'
    login_url = '/user/login'

    def get_queryset(self):
        queryset = self.model.objects.filter(userprofile__user=self.request.user, history__is_favorite=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FavoritesListView, self).get_context_data(**kwargs)
        data = cargar_info_usuario(self.request)
        context['data'] = data
        return context


def reset_password_view(request):
    data = {}
    if request.method == 'POST':
        username = request.POST.get('user', '')
        if username:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = None
                data = {'error': 'Ingresa un username valido'}
            if user:
                contra = User.objects.make_random_password(length=16)
                user.set_password(contra)
                user.save()
                print(contra)
                data = {'mensaje': 'Revisa tu correo electronico e intenta iniciar sesion'}
                subject = 'Recuperar contraseña'
                message_text = 'PlayFilms,'
                message_html = '<p>Hola <strong>%s</strong>, tu nueva contraseña es: <strong>%s</strong></p>' % (
                    username, contra)
                FROM_EMAIL = '"PlayFilms" <playfilms.email@gmail.com>'
                destination = user.email
                send_email(subject, message_text, message_html, FROM_EMAIL, destination)
        else:
            data = {'error': 'Ingresa un username valido'}
    return render(request, 'recuperar_contra.html', {'data': data})


def send_email(subject, message, html, from_email, destination):
    try:
        msg = EmailMultiAlternatives(subject, message, from_email, [destination])
        msg.attach_alternative(html, "text/html")
        msg.send()
    except BadHeaderError:
        return HttpResponse('Invalid header found.')


@login_required(login_url='/user/login/')
def profile_view(request):
    data = cargar_info_usuario(request)
    user = User.objects.get(username=request.user.username)
    profile = user.userprofile
    card = profile.creditcard
    uform = UserForm(request.POST or None, instance=user)
    pform = UserProfileForm(request.POST or None, request.FILES, instance=profile)
    cform = CreditCardForm(request.POST or None, instance=card)

    if request.POST and cform.is_valid():
        new_card = cform.save()
        new_profile = profile
        validar_tarjeta(new_card, new_profile)
        uform = UserForm(instance=user)
        prepare_email_data(user)
    else:
        if request.method == 'POST':
            if pform.is_valid():
                pform.save()
                prepare_email_data(user)
        if request.POST and uform.is_valid():
            new_user = uform.save()
            cform = CreditCardForm(instance=new_user.userprofile.creditcard)
            login(request, new_user)
            prepare_email_data(new_user)
        else:
            uform = UserForm(instance=user)

    return render(request, 'profile.html', {'uform': uform, 'pform': pform, 'cform': cform, 'data': data})


def prepare_email_data(user):
    subject = 'Modificación de datos personales'
    message_text = 'PlayFilms,'
    message_html = '<p>Hola <strong>%s</strong>, se han modificado algunos datos de tu cuenta.</p>' % (
        user.first_name)
    FROM_EMAIL = '"PlayFilms" <playfilms.email@gmail.com>'
    destination = user.email
    send_email(subject, message_text, message_html, FROM_EMAIL, destination)

def borrar_view(request):
    if request.method=='POST':
        user = request.user
        user.is_active = False
        user.save()
    return redirect('/user/logout')