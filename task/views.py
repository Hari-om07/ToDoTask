from django.shortcuts import render, redirect
from .models import Task
from .forms import Taskforms

# Create your views here.
def task_list(request):
    task = Task.objects.all()
    return render(request, 'task_list.html', {'task':task})

def task_create(request):
    if request.method == "POST":
        form = Taskforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        
    else:
        form = Taskforms()
    return render(request, 'task_form.html', {'form': form})

def task_clear(request):
    Task.objects.all().delete()  
    return redirect('task_list')