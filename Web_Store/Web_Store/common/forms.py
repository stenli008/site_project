from django import forms

from Web_Store.common.models import Shipping


class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = ('address', 'city')
