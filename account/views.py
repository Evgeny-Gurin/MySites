from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.views import View
from django.template.context_processors import csrf
# Create your views here.


def home(request):
    return render(request, 'account/home.html')


def login_redirect(request, site_redirect='menu'):
    context = {}
    context.update(csrf(request))

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(site_redirect)
        else:
            context['login_error'] = 'Пожалуйста, введите корректные адрес электронной почты и пароль учётной записи.' \
                                     ' Оба поля могут быть чувствительны к регистру.'
            return render_to_response('account/login.html', context)
    else:
        return render_to_response('account/login.html', context)


# @login_required(login_url='/account/login')
# def profile(request):
#     return redirect('')
#
#


# from .forms import UserForm, UserExtendedForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
#
#
# def home(request):
#     return redirect(auth_app_home)
#
#
# @login_required(login_url='/test_account/auth-app/login')
# def auth_app_home(request):
#     return render(request, 'test_account/../../account/templates/account/home1.html')
#
#
# def auth_app_sign_up(request):
#     context = {
#         'user_form': UserForm(),
#         'user_extended_form': UserExtendedForm()
#     }
#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#         user_extended_form = UserExtendedForm(request.POST, request.FILES)
#
#         if user_form.is_valid() and user_extended_form.is_valid():
#
#             new_user = User.objects.create_user(**user_form.cleaned_data)
#             new_user_extended = user_extended_form.save(commit=False)
#             new_user_extended.user = new_user
#             new_user_extended.save()
#
#             login(request, authenticate(
#                 username=user_form.cleaned_data['username'],
#                 password=user_form.cleaned_data['password'],
#             ))
#
#             return redirect(auth_app_home)
#
#     return render(request, 'test_account/../../account/templates/account/sign_up.html', context)


# def login(request):
#     return render(request, 'test_account/login1.html', {})
#
#
# class CreationView(View):
#     context = {
#         'user_form': UserForm(),
#         'user_extended_form': UserExtendedForm()
#     }
#
#     def get(self, request):
#         return render(request, "test_account/creation1.html", self.context)
#
#     def post(self, request):
#
#         user_form = UserForm(request.POST)
#         user_extended_form = UserExtendedForm(request.POST, request.FILES)
#
#         if user_form.is_valid() and user_extended_form.is_valid():
#
#             # user_extended = user_extended_form.save(commit=False)
#             # user_extended.user = user_form.user
#             # user_extended.save()
#             user_form.save()
#             return redirect('home')
#         else:
#             return render(request, "test_account/creation1.html", self.context)
