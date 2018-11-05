from django.urls import path
from myapp import views

routes = [
    path('roles/', views.RolesListView.as_view(), name='roles')
]
