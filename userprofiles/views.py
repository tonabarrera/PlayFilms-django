from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView, RedirectView, ListView

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

class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/catalogo/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/catalogo/')
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

def signUp_view(request):
    if request.method == 'POST':
        uform = UserForm(request.POST)
        pform = UserProfileForm(request.POST)
        cform = CreditCardForm(request.POST)
        print('post')
        if uform.is_valid() and pform.is_valid() and cform.is_valid():
            user = uform.save()
            profile = pform.save(commit=False)
            card = cform.save(commit=False)
            profile.user = user
            profile.save()
            card.user_profile = profile
            card.save()
            print('Se registro')
            login(request, user)
            return redirect('/catalogo/')
    else:
        uform = UserForm()
        pform = UserProfileForm()
        cform = CreditCardForm()
    return render(request, 'signup.html', {'uform': uform, 'pform':pform, 'cform':cform})
def logout_view(request):
    logout(request)
    return redirect('/user/login')


class LoginRedirectView(RedirectView):
    permanent = True
    pattern_name = 'user:login'

class FavoritesListView(LoginRequiredMixin, ListView):
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
                message_html = '<p>Hola <strong>%s</strong>, tu nueva contraseña es: <strong>%s</strong></p>' % (username, contra)
                from_email = '"PlayFilms" <playfilms.email@gmail.com>'
                destination = user.email
                try:
                    msg = EmailMultiAlternatives(subject, message_text, from_email, [destination])
                    msg.attach_alternative(message_html, "text/html")
                    msg.send()
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
        else:
            data = {'error': 'Ingresa un username valido'}
    return render(request, 'recuperar_contra.html', {'data': data})