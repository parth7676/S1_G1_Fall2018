from django.urls import path, re_path
from myapp.partials_views import roles

routes = [
    path('roles/', roles.RolesListView.as_view(), name='roles'),
    path('role/add/', roles.role_create_view, name='add-role'),
    re_path(r'^role/edit/(?P<role_id>[0-9]+)/$', roles.role_update_view, name='update-role')
]
