from django.urls import path, re_path
from myapp.partials_views import advertisements

routes = [
    path('advertisements/', advertisements.create_advertisement, name='advertisements'),
]