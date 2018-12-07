from django import forms
from myapp.models import Advertisement, Property


class CreateAdvertisementForm(forms.ModelForm):
    property = forms.ModelMultipleChoiceField(queryset=Property.objects.all(), to_field_name='propertyTitle', required=True)

    class Meta:
        model = Advertisement
        fields = [
            'advStartDate', 'advEndDate', 'advDescription', 'property'
        ]
