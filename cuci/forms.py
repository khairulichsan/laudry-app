from django import forms
from .models import CuciOrder

class CuciOrderForm(forms.ModelForm):
    class Meta:
        model = CuciOrder
        fields = ['customer_name', 'service_type', 'price', 'status','debt']
