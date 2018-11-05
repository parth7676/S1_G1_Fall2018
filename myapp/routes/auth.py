from django.urls import path
from myapp.partials_views import auth

routes = [
    path('login/', auth.sign_in, name="login"),
    path('register/', auth.register, name="register"),
]
