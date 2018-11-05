from django.forms import ModelForm
from .models import *
from django.utils.translation import gettext_lazy as _


class RoleForm(ModelForm):
    class Meta:
        model = RoleCode
        fields = ['roleName', 'code']
        labels = {
            'roleName': _('Role Name'),
            'code': _('Code')
        }
