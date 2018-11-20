from django import forms
from myapp.models import PermissionType, PermissionTypeChoices


class CreatePermissionForm(forms.ModelForm):
    name = forms.Select(choices=[(tag.value, tag.name) for tag in PermissionTypeChoices])

    class Meta:
        model = PermissionType
        fields = ['name']
