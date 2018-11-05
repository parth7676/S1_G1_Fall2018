from django.views import generic
from myapp.models import RolePermission
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from myapp.forms.features import CreateFeatureForm


class FeaturesListView(generic.ListView):
    template_name = 'account/features.html'
    context_object_name = 'features'

    def get_queryset(self):
        permissions = RolePermission.objects.select_related('code').all()
        paginator = Paginator(permissions, 9)
        page = self.request.GET.get('page')
        return paginator.get_page(page)


def create_feature_view(request):
    form = CreateFeatureForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('features')

    context = {
        'form': form,
        'isEdit': False
    }
    return render(request, 'account/feature_form.html', context)


def update_feature_view(request, role_permission_id):
    feature = RolePermission.objects.get(rolePermissionID=role_permission_id)
    form = CreateFeatureForm(request.POST or None, instance=feature)
    if form.is_valid():
        form.save()
        return redirect('features')

    context = {
        'form': form,
        'isEdit': True
    }
    return render(request, 'account/feature_form.html', context)
