from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'
        Todo.objects.create(title=title, description=description, completed=completed)
        return redirect('todo_list')
    return render(request, 'todo_create.html')

def todo_update(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.completed = request.POST.get('completed') == 'on'
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo_update.html', {'todo': todo})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_delete.html', {'todo': todo})
