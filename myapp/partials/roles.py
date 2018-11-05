from django.views import generic
from myapp.models import RoleCode
from django.views.generic import DeleteView
from django.urls import reverse_lazy


class RolesListView(generic.ListView):
    template_name = 'account/roles.html'
    context_object_name = 'roles'

    def get_queryset(self):
        return RoleCode.objects.all()


class RoleDelete(DeleteView):
    model = RoleCode
    success_url = reverse_lazy('roles')
