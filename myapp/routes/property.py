from django.urls import path, re_path
from myapp import views

routes = [
    path('search-property/', views.SearchPropertyView.as_view(), name="search-property"),
    path('advertise-property/', views.advertise_property, name="advertise-property"),
    re_path(r'^details/(?P<propertyID>[0-9]+)/$', views.property_details, name="property-details"),
]
