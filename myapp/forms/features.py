from django.forms import ModelForm
from myapp.models import RolePermission
from django.utils.translation import gettext_lazy as _


class CreateFeatureForm(ModelForm):
    class Meta:
        model = RolePermission
        fields = ['sysFeature', 'code', 'permissions']
        labels = {
            'sysFeature': _('System Feature'),
            'code': _('Role'),
            'permissions': _('Permissions')
        }