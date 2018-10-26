from django.shortcuts import render
from django.views import generic
from myapp.models import *
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def advertise_property(request):
    return render(request, 'advertiseproperty.html')


def contact(request):
    return render(request, 'contactus.html')


def register(request):
    return render(request, 'register.html')


def sign_in(request):
    return render(request, 'login.html')


def property_details(request, propertyID):
    return render(request, 'propertydetails.html')

# class PropertyDetail(generic.DetailView):
#     template_name = 'searchproperty.html'
#     context_object_name = 'detail'
#
#     def get_queryset(self):



def account(request):
    return render(request, 'account/accountBase.html')


class UsersView(generic.ListView):
    template_name = 'account/users.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()


class SearchPropertyView(generic.ListView):
    template_name = 'searchproperty.html'
    context_object_name = 'properties'

    def get_queryset(self):
        property_list = Property.objects.all().select_related('propertyProvince', 'propertyCountry', 'propertyCity')
        paginator = Paginator(property_list, 9)
        page = self.request.GET.get('page')
        return paginator.get_page(page)
