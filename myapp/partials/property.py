from django.shortcuts import render
from django.views import generic
from myapp.models import Property
from django.core.paginator import Paginator


def advertise_property(request):
    return render(request, 'advertiseproperty.html')


def property_details(request, propertyID):
    return render(request, 'propertydetails.html')


# class PropertyDetail(generic.DetailView):
#     template_name = 'searchproperty.html'
#     context_object_name = 'detail'
#
#     def get_queryset(self):


class SearchPropertyView(generic.ListView):
    template_name = 'searchproperty.html'
    context_object_name = 'properties'

    def get_queryset(self):
        property_list = Property.objects.all().select_related('propertyProvince', 'propertyCountry', 'propertyCity') \
            .order_by('propertyID')
        paginator = Paginator(property_list, 9)
        page = self.request.GET.get('page')
        return paginator.get_page(page)

