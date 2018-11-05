from django.urls import path
from myapp.partials_views import accounts

routes = [
    path('users/', accounts.UsersView.as_view(), name='users'),
    path('users/activate/', accounts.activate_user)
]
