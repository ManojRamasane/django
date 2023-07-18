from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import CustomTodo
from django.views import View
from .forms import CustomTodoForm

# Create your views here.
def todoList(request):
    tasks = CustomTodo.objects.all()
    return render(request, 'html/home.html', {'tasks': tasks})

def show_pending_task(request):
    incomplete_tasks = CustomTodo.objects.filter(is_completed=False)
    return render(request, 'html/home.html', {'tasks': incomplete_tasks})

class CreateTodoTaskView(View):
    def get(self, request):
        form = CustomTodoForm()
        return render(request, 'html/createTask.html', {'form': form})
    
    def post(self, request):
        form = CustomTodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            user = form.cleaned_data['user']
            is_completed = form.cleaned_data['is_completed']
            todo_task = CustomTodo(
                title=title,
                description=description,
                start_date=start_date,
                end_date=end_date,
                user=user,
                is_completed=is_completed
            )

            todo_task.save()
            messages.success(request, 'Todo task created successfully.')
            return redirect('todoList')
        return render(request, 'html/createTask.html', {'form': form})
    
def edit_task(request, task_id):
    task = get_object_or_404(CustomTodo, id=task_id)

    if request.method == 'POST':
        form = CustomTodoForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.start_date = form.cleaned_data['start_date']
            task.end_date = form.cleaned_data['end_date']
            task.user = form.cleaned_data['user']
            task.is_completed = form.cleaned_data['is_completed']
            task.save()
            messages.success(request, 'Your Todo task edited successfully.')
            return redirect('todoList')  # Redirect to the desired page after successful editing
    else:
        form = CustomTodoForm(initial={
            'title': task.title,
            'description': task.description,
            'start_date': task.start_date,
            'end_date': task.end_date,
            'user': task.user,
            'is_completed': task.is_completed
        })
    
    return render(request, 'html/editTask.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(CustomTodo, id=task_id)
    task.delete()
    messages.error(request, 'Your Todo task deleted successfully.')
    return redirect('todoList')

