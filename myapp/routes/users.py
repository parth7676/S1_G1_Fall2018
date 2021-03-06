from django.urls import path, re_path
from myapp.partials_views import accounts
from myapp.decorators import admin_only

routes = [
    path('users/', admin_only(accounts.UsersView.as_view()), name='users'),
    path('users/activate/', accounts.activate_user, name='user-activate'),
    path('users/add/', accounts.user_create_view, name='add-user'),
    re_path(r'^users/edit/(?P<user_id>[0-9]+)/$', accounts.user_edit_view, name='update-user'),
    re_path(r'^user/delete/(?P<user_id>[0-9]+)/$', accounts.user_delete_view, name='delete-user')
]
