from django.shortcuts import render, redirect

from shop.forms.category_form import CategoryForm

def category_add_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = CategoryForm()
    return render(request, 'catalog/categories/create.html', {'form': form})
