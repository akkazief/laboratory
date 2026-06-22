from django import forms

from shop.models.order import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['username', 'phone', 'address']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }