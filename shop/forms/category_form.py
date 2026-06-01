from django import forms

from shop.models.category import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'}),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
            'placeholder': 'Введите описание'}),
        }