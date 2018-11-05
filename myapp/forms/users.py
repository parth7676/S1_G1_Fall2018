from django import forms
from myapp.models import User


class CreateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email']


class ActiveStatusForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['isActive']


class UserFormWithPassword(CreateUserForm):

    password = forms.CharField(widget=forms.TextInput(), required=False)

    class Meta(CreateUserForm.Meta):
        fields = CreateUserForm.Meta.fields + ['password']
