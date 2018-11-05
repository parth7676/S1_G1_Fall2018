from django.urls import path, re_path
from myapp.partials_views import accounts

routes = [
    path('users/', accounts.UsersView.as_view(), name='users'),
    path('users/activate/', accounts.activate_user),
    re_path(r'^users/edit/(?P<user_id>[0-9]+)/$', accounts.user_edit_view, name='update-user')
]
