from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm, RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # получить объект User из формы, без сохранения в бд
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'first_name': new_user.first_name})
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'register_form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = auth.authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('account', user_id=user.id)
                else:
                    return render(request, 'account/error.html', {'text': 'аккаунт не активен... :('})
            else:
                form = LoginForm()
                return render(request, 'account/login.html', {'form': form, 'error': True})
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('home')


def account(request, user_id):
    if not request.user.is_authenticated:
        return redirect('home')
    user = None
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        pass
    return render(request, 'account/index.html', {'user': user})
