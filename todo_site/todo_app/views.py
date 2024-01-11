from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoFrom, todoForm
from .models import Todo, Todos
from django.http import HttpResponse
# Create your views here.


def index(request):
    if request.method == 'POST':
        title = request.POST.get('title') 
        todo = Todos.objects.create(title=title)
        todo.save()
        return redirect(index)
    
    todo_list = Todos.objects.all().order_by('-id')
    return render(request, 'index.html', {'todo_list': todo_list})

def mark_todo(request, pk):
    todo = Todos.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    todo_list = Todos.objects.all().order_by('-id')
    return render(request, 'index.html', {'todo_list': todo_list})

def delete_todo(request, pk):
    todo = Todos.objects.get(pk=pk)
    todo.delete()
    todo_list = Todos.objects.all().order_by('-id')
    return render(request, 'index.html', {'todo_list': todo_list})

def edit_todo(request, pk):
    if request.method == 'POST':
        todo = Todos.objects.get(pk=pk)
        title = request.POST.get('title') 
        todo = title(request.POST or None, instance=title)
        todo.save()
    todo = Todos.objects.get(pk=pk)
    return render(request, 'edit.html', {'todo': todo})

def home(request):

    return render(request, 'home.html')