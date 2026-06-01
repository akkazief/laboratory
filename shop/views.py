from django.shortcuts import render, redirect,get_object_or_404

from shop.models.product import Product
from shop.forms import TaskForm


def tasks(request):
    tasks = Product.objects.all()
    context = {'shop': tasks}
    return render(request, 'shop/shop.html', context)

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = TaskForm()
    return render(request, 'shop/create_task.html', {'form': form})

def delete_task(request, pk):
    task = Product.objects.get(id=pk)
    task.delete()
    return redirect('main')

def details(request, *args, pk, **kwargs):
    task = get_object_or_404(Product, pk=pk)
    context = {'task': task}
    return render(request, "shop/details.html", context)