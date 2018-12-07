from django.urls import path, re_path
from myapp.partials_views import permissions

routes = [
    path('permissions/', permissions.PermissionsListView.as_view(), name='permissions'),
    path('permissions/add/', permissions.create_permission_view, name='add-permission'),
    re_path(r'^permissions/delete/(?P<permission_id>[0-9]+)/$',
            permissions.permission_delete_view, name='delete-permission')
]

