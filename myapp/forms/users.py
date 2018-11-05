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
