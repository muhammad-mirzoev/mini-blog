from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import (
    UserRegistrationForm,
    UserLoginForm,
    UserProfileUpdateForm,
)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    form = UserRegistrationForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Регистрация прошла успешно')
        return redirect('accounts:profile')

    return render(request, 'accounts/register.html', {
        'form': form
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        login(request, form.cleaned_data['user'])
        messages.success(request, 'Вы вошли в систему')
        return redirect('accounts:profile')

    return render(request, 'accounts/login.html', {
        'form': form
    })


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Вы вышли из системы')
    return redirect('accounts:login')


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {
        'user_obj': request.user
    })


@login_required
def profile_edit_view(request):
    form = UserProfileUpdateForm(
        request.POST or None,
        request.FILES or None,
        instance=request.user
    )

    if form.is_valid():
        form.save()
        messages.success(request, 'Профиль обновлён')
        return redirect('accounts:profile')

    return render(request, 'accounts/profile_edit.html', {
        'form': form
    })
