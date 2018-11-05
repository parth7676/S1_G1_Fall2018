from django.urls import path
from myapp import views

routes = [
    path('features/', views.FeaturesListView.as_view(), name='features')
]

