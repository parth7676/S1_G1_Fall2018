from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def SearchProperty(request):
    return render(request, 'searchproperty.html')

def AdvertiseProperty(request):
    return render(request, 'advertiseproperty.html')

def Contact(request):
    return render(request, 'contactus.html')

def Register(request):
    return render(request, 'register.html')

def Signin(request):
    return render(request, 'login.html')
