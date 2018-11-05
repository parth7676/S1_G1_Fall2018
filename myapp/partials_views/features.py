from django.views import generic
from myapp.models import RolePermission
from django.core.paginator import Paginator


class FeaturesListView(generic.ListView):
    template_name = 'account/features.html'
    context_object_name = 'features'

    def get_queryset(self):
        permissions = RolePermission.objects.select_related('code').all()
        paginator = Paginator(permissions, 9)
        page = self.request.GET.get('page')
        return paginator.get_page(page)

