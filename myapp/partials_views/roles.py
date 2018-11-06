from django.shortcuts import redirect, render
from django.views import generic
from myapp.models import RoleCode
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from myapp.forms.roles import CreateRoleForm, DeleteRoleForm


class RolesListView(generic.ListView):
    template_name = 'account/roles.html'
    context_object_name = 'roles'

    def get_queryset(self):
        return RoleCode.objects.all()


class RoleDelete(DeleteView):
    model = RoleCode
    success_url = reverse_lazy('roles')


def role_create_view(request):
    form = CreateRoleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('roles')

    context = {
        'form': form,
        'isEdit': False
    }
    return render(request, 'account/role_form.html', context)


def role_update_view(request, role_id):
    role = RoleCode.objects.get(id=role_id)
    form = CreateRoleForm(request.POST or None, instance=role)
    if form.is_valid():
        form.save()
        return redirect('roles')

    context = {
        'form': form,
        'isEdit': True
    }
    return render(request, 'account/role_form.html', context)


def role_delete_view(request, role_id):
    data = RoleCode.objects.filter(id=role_id).first()
    if not data:
        data.delete()
        return redirect('roles')





