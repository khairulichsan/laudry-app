from django import forms
from .models import InputCustomer
from .models import CuciOrder

class InputCostumerForm(forms.ModelForm):
    class Meta:
        model = InputCustomer
        fields = ['name','nomor_hp', 'alamat']


class CuciOrderForm(forms.ModelForm):
    class Meta:
        model = CuciOrder
        fields = ['customer','service_type', 'price', 'status','debt']
