from django.urls import path
from myapp.partials import roles

routes = [
    path('roles/', roles.RolesListView.as_view(), name='roles')
]
