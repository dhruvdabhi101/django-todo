from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo

# Create your views here.
def index(request):
    tasks = Todo.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request,'index.html',context)

def all_tasks(request):
    tasks = Todo.objects.all()
    context = {
        'tasks': tasks
    }
    return HttpResponseRedirect('/')

def add(request):
    if request.method == 'POST':
        task = request.POST['task']
        new_task = Todo(task=task)
        new_task.save()
        return HttpResponseRedirect('all_tasks')
    else:
        return render(request,'index.html',{'error':'Invalid Input'})
    
def delete_task(request,id):
    task = Todo.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect('/')