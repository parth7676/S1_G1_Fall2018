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

    role = forms.ChoiceField(widget=forms.Select(), required=True, choices=[
        (role.roleName, role.roleName) for role in RoleCode.objects.all()
    ])

    class Meta(CreateUserForm.Meta):
        fields = CreateUserForm.Meta.fields + ['password', 'role']
