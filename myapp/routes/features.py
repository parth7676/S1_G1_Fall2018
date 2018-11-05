from django.urls import path
from myapp.partials_views import features

routes = [
    path('features/', features.FeaturesListView.as_view(), name='features')
]

