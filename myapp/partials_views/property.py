from django.shortcuts import render
from django.views import generic
from myapp.models import Property
from django.core.paginator import Paginator


def advertise_property(request):
    return render(request, 'advertiseproperty.html')


def property_details(request, propertyID):
    property_item = Property.objects.filter(propertyID=propertyID).select_related('propertyCity').first()
    print(property_item)
    return render(request, 'propertydetails.html', {'property': property_item})


# class PropertyDetail(generic.DetailView):
#     template_name = 'searchproperty.html'
#     context_object_name = 'detail'
#
#     def get_queryset(self):


class SearchPropertyView(generic.ListView):

    template_name = 'searchproperty.html'
    context_object_name = 'properties'

    def get_queryset(self):
        if 'search' in self.request.GET:
            property_list = Property.objects.filter(propertyCity__cityName__contains=self.request.GET.get('search'))\
                .select_related('propertyProvince', 'propertyCountry', 'propertyCity') \
                .order_by('propertyID')
        else:
            property_list = Property.objects.all() \
                .select_related('propertyProvince', 'propertyCountry', 'propertyCity') \
                .order_by('propertyID')
        paginator = Paginator(property_list, 9)
        page = self.request.GET.get('page')
        return paginator.get_page(page)

