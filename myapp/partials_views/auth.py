from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect


def register(request):
    return render(request, 'register.html')


def sign_in(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        auth_user = authenticate(request, username=email, password=password)
        if auth_user is not None:
            login(request, auth_user)
            return redirect('/')
    else:
        if not isinstance(request.user, AnonymousUser):
            return redirect('/')
        else:
            return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')
