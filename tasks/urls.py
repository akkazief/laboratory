from django.urls import path
from tasks.views import tasks, create_task, delete_task, details

urlpatterns = [
    path('', tasks, name='main'),
    path('create_task/', create_task, name='create_task'),
    path('tasks/delete_task/<int:pk>/', delete_task, name='delete_task'),
    path('tasks/<int:pk>/', details, name='details'),
]