from django.shortcuts import render, redirect,get_object_or_404

from shop.models.product import Product
from shop.forms.product_form import ProductForm
from shop.forms.search_form import SearchForm
from shop.models.category import Category



def products_view(request):
    search = SearchForm(request.GET)
    products = Product.objects.filter(stock__gte=1).order_by('category', 'name')
    categories = Category.objects.all().order_by('name')

    if search.is_valid():
        query = search.cleaned_data.get('query')
        if query:
            products = products.filter(name__icontains=query)

    context = {'products': products,
               'search': search,
               'categories': categories,
               'create_form': ProductForm(),
               }

    return render(request, "catalog/products/list_all.html", context)

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, "catalog/products/detail.html", context)

def product_add_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_view', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'catalog/products/create.html', {'form': form})

def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('main')
    return render(request, 'catalog/products/delete.html', {'product': product})

def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = ProductForm(instance=product)
    return render(request, 'catalog/products/update.html', {'form': form, 'product': product})

def products_by_category(request, category_name):
    search = SearchForm(request.GET)
    products = Product.objects.filter(stock__gte=1, category__name=category_name).order_by('name')
    categories = Category.objects.all().order_by('name')

    if search.is_valid():
        query = search.cleaned_data.get('query')
        if query:
            products = products.filter(name__icontains=query)

    context = {'products': products,
               'search': search,
               'categories': categories,
               'category_name': category_name,
               'create_form': ProductForm(),
               }
    return render(request, "catalog/products/list_by_categories.html", context)
