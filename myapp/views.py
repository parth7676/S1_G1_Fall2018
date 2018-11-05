from django.shortcuts import render
from django.views import generic
from myapp.models import *
from django.core.paginator import Paginator
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


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
        users_list = User.objects.all().order_by('userID')
        paginator = Paginator(users_list, 10)
        page = self.request.GET.get('page')
        return paginator.get_page(page)


class UserCreate(CreateView):
        model = User
        fields = ['firstName', 'lastName', 'email']


class SearchPropertyView(generic.ListView):
    template_name = 'searchproperty.html'
    context_object_name = 'properties'

    def get_queryset(self):
        property_list = Property.objects.all().select_related('propertyProvince', 'propertyCountry', 'propertyCity')\
            .order_by('propertyID')
        paginator = Paginator(property_list, 9)
        page = self.request.GET.get('page')
        return paginator.get_page(page)


class FeaturesListView(generic.ListView):
    template_name = 'account/features.html'
    context_object_name = 'features'

    def get_queryset(self):
        permissions = RolePermission.objects.select_related('code').all()
        paginator = Paginator(permissions, 9)
        page = self.request.GET.get('page')
        return paginator.get_page(page)


class RolesListView(generic.ListView):
    template_name = 'account/roles.html'
    context_object_name = 'roles'

    def get_queryset(self):
        return RoleCode.objects.all()


class RoleDelete(DeleteView):
    model = RoleCode
    success_url = reverse_lazy('roles')
