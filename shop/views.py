from django.shortcuts import render, redirect,get_object_or_404

from shop.models.product import Product
from shop.forms.product_form import ProductForm
from shop.forms.category_form import CategoryForm


def products_view(request):
    products = Product.objects.all()
    context = {'shop': products}
    return render(request, 'catalog/products.html', context)

def product_view(request, pk):
    task = get_object_or_404(Product, pk=pk)
    context = {'task': task}
    return render(request, "catalog/product_details.html", context)

def category_add_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = CategoryForm()
    return render(request, 'catalog/add_category.html', {'form': form})

def product_add_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})


# def delete_product(request, pk):
#     task = Product.objects.get(id=pk)
#     task.delete()
#     return redirect('main')

