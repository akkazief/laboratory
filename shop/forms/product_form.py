from django import forms
from shop.models.product import Product


class ProductForm(forms.ModelForm):

    stock = forms.IntegerField(
        min_value=0,
        label="Остаток",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите остаток',
        })
    )
    price = forms.DecimalField(
        max_digits=7,
        decimal_places=2,
        label="Стоимость",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите стоимость товара'
        })
    )

    class Meta:
        model = Product
        fields = ('name', 'description' ,'category', 'price', 'img', 'stock')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Поле для детального описания'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'img': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на изображение'
            })
        }
