from django.shortcuts import render


def register(request):
    return render(request, 'register.html')


def sign_in(request):
    return render(request, 'login.html')

