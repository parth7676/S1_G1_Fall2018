from django import forms
from myapp.models import User, RoleCode


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email']


class ActiveStatusForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['isActive']


class UserFormWithRelatedFields(CreateUserForm):

    password = forms.CharField(widget=forms.TextInput(), required=False)

    role = forms.ModelChoiceField(required=True, queryset=RoleCode.objects.all(),
                                  empty_label=None, to_field_name='roleName')

    class Meta(CreateUserForm.Meta):
        fields = CreateUserForm.Meta.fields + ['password', 'role']
