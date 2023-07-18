from django.urls import path

from .views import *




urlpatterns = [

    path('', todoList, name='todoList'),
    path('pending/', show_pending_task,name='show_pending_task'),
    path('createTask/', CreateTodoTaskView.as_view(), name='createTask'),
    path('editTask/<uuid:task_id>/', edit_task, name='edit_task'),
    path('deleteTask/<uuid:task_id>/', delete_task, name='delete_task'),

]