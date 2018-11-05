from django import forms
from myapp.models import User


class ActiveStatusForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['isActive']
