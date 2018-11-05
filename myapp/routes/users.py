from django.urls import path, re_path
from myapp.partials import accounts

routes = [
    path('users/', accounts.UsersView.as_view(), name='users'),
    path('users/activate', accounts.activate_user)
]
