from django.shortcuts import render, redirect,get_object_or_404

from shop.models.product import Product
from shop.forms.product_form import ProductForm
from shop.forms.category_form import CategoryForm


def products_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/products.html', context)

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, "catalog/product_view.html", context)

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
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_view', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})

def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('main')
    return render(request, 'catalog/delete_product.html', {'product': product})

def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = ProductForm(instance=product)
    return render(request, 'catalog/update_product.html', {'form': form, 'product': product})
