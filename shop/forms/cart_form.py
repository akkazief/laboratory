from django import forms

class AddToCartForm(forms.Form):
    amount = forms.IntegerField(min_value=1, initial=1, label="")
