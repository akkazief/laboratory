from django import forms
from shop.models.product import Product


class ProductForm(forms.ModelForm):
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
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите стоимость товара'
            }),
            'img': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на изображение'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите остаток'
            })
        }

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError("Остаток не может быть меньше 0")
        return stock

