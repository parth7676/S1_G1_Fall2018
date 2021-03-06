from django.urls import path, re_path
from myapp.partials_views import property

routes = [
    path('search-property/', property.SearchPropertyView.as_view(), name="search-property"),
    re_path(r'^details/(?P<propertyID>[0-9]+)/$', property.property_details, name="property-details"),
]
