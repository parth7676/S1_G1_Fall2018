from django.views import generic
from myapp.models import PermissionType
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from myapp.forms.permissions import CreatePermissionForm
from django.http import HttpResponseRedirect


class PermissionsListView(generic.ListView):
    template_name = 'account/permissions.html'
    context_object_name = 'permissions'

    def get_queryset(self):
        permissions = PermissionType.objects.all()
        paginator = Paginator(permissions, 9)
        page = self.request.GET.get('page')
        return paginator.get_page(page)


def create_permission_view(request):
    form = CreatePermissionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('permissions')

    context = {
        'form': form,
        'isEdit': False
    }
    return render(request, 'account/permission_form.html', context)


def permission_delete_view(request, permission_id):
    feature = PermissionType.objects.filter(id=permission_id)

    if feature:
        feature.delete()
        return HttpResponseRedirect('/features/')

