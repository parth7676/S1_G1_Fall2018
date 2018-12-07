from django.urls import path
from myapp.partials_views import advertisements

routes = [
    path('advertise-property/', advertisements.create_advertisement, name="advertise-property"),
]