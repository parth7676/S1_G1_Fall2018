from myapp import views
from django.urls import path, re_path
from myapp.partials_views import accounts
from myapp.routes import auth, features, property, roles, users, permissions

includeRoutes = [auth, users, roles, property, features, permissions]

urlPatterns = [
    re_path(r'^$', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('account/', accounts.account, name="account")
]

for route in includeRoutes:
    for route_path in route.routes:
        urlPatterns.append(route_path)
