from django import forms
from shop.models.product import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description' ,'category', 'price', 'img')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше описание',}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Поле для детального описания'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите стоимость товара'
            }),
            'img': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'поле для вашего изображения'
            })
        }

