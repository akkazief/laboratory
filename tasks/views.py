from django.shortcuts import render, redirect,get_object_or_404, reverse

from tasks.models import Task
from tasks.forms import TaskForm


def tasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/tasks.html', context)

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('main')

def details(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, "tasks/details.html", context)