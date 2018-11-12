from django.urls import path, re_path
from myapp.partials_views import features

routes = [
    path('features/', features.FeaturesListView.as_view(), name='features'),
    path('features/add/', features.create_feature_view, name='add-feature'),
    re_path(r'^features/edit/(?P<role_permission_id>[0-9]+)/$', features.update_feature_view, name='update-feature'),
    re_path(r'^feature/delete/(?P<role_permission_id>[0-9]+)/$', features.feature_delete_view, name='delete-feature')
]

