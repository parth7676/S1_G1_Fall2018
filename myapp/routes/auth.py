from django.urls import path
from myapp import views

routes = [
    path('login/', views.sign_in, name="login"),
    path('register/', views.register, name="register"),
]
