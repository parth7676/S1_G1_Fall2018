from myapp import views
from django.urls import path, re_path

urlPatterns = [
    re_path(r'^$', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('search-property/', views.SearchPropertyView.as_view(), name="search-property"),
    path('advertise-property/', views.advertise_property, name="advertise-property"),
    path('login/', views.sign_in, name="login"),
    path('register/', views.register, name="register"),
    path('contact/', views.contact, name="contact"),
    re_path(r'^details/(?P<propertyID>[0-9]+)/$', views.property_details, name="property-details"),
    path('account/', views.account, name='account'),
    path('users/', views.UsersView.as_view(), name='users'),
    path('features/', views.FeaturesListView.as_view(), name='features'),
    path('roles/', views.RolesListView.as_view(), name='roles'),
    path('role/add/', views.role_create_view, name='add-role'),
    re_path(r'^role/edit/(?P<role_id>[0-9]+)/$', views.role_update_view, name='update-role')
]
