from django import forms
from .models import Orders

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

        labels = {
            'oid': 'Order ID',
            'fname': 'Frist name',
            'lname': 'Last Name',
            'price': 'Price',
            'mail_addr': 'Email Id',
            'addr': 'Address',
        }

        widgets = {
            'oid': forms.NumberInput(attrs={
                'placeholder': 'Order ID',
            }),
            'fname': forms.TextInput(attrs={
                'placeholder': 'Enter First Name',
            }),
            'lname': forms.TextInput(attrs={
                'placeholder': 'Enter Last Name',
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': '10.00',
            }),
            'mail_addr': forms.EmailInput(attrs={
                'placeholder': 'example@gmail.com',
            }),
            'addr': forms.TextInput(attrs={
                'placeholder': 'Address',
            }),
        }
