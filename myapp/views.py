from django.shortcuts import render
from myapp.models import Property


def home(request):
    properties = Property.objects.select_related('propertyCity', 'propertyUser')[:3]
    return render(request, 'home.html', {'properties': properties})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contactus.html')