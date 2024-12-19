from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import TodoForm, TodoFilterForm
from .models import Todo
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # Import User model

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homeView')  # Redirect to the homepage
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'todo/login.html')

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homeView')  # Redirect to the homepage
    else:
        form = UserCreationForm()
    return render(request, 'todo/signup.html', {'form': form})

# Home view (after login)
@login_required
def homeView(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()

            messages.success(request, 'Task Added To Todo List Successfully!')
            return redirect(homeView)
    else:
        form = TodoForm()

    # Filter tasks based on status
    filter_form = TodoFilterForm(request.POST or None)
    if filter_form.is_valid():
        filter_status = filter_form.cleaned_data['status']
        if filter_status == 'all':
            todoList = Todo.objects.filter(user=request.user).order_by('completed')
        elif filter_status == 'completed':
            todoList = Todo.objects.filter(user=request.user, completed=True)
        else:
            todoList = Todo.objects.filter(user=request.user, completed=False)
    else:
        todoList = Todo.objects.filter(user=request.user).order_by('completed')

    return render(request, 'todo/index.html', {
        'todoList': todoList,
        'form': form,
        'filter_form': filter_form
    })

# Complete or uncomplete task view
def completeTaskView(request, id):
    task = get_object_or_404(Todo, id=id)
    if task.completed:
        task.completed = False
        messages.error(request, 'Marked Task As Uncompleted.')
    else:
        task.completed = True
        messages.success(request, 'Marked Task As Completed.')
    task.save()
    return redirect(homeView)

# Edit task view
def editTaskView(request, id):
    task = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.info(request, 'Task Edited')
            return redirect(homeView)
    else:
        form = TodoForm(instance=task)
    todoList = Todo.objects.all().order_by('completed').exclude(id=id)
    return render(request, 'todo/index.html', context={
        'todoList': todoList,
        'form': form
    })

# Delete specific task view
def deleteTaskView(request, id):
    task = get_object_or_404(Todo, id=id)
    task.delete()
    messages.error(request, 'Task Deleted.')
    return redirect(homeView)

# Delete all tasks view
def deleteAllTaskView(request):
    BATCH_SIZE = 100
    for task in Todo.objects.iterator(chunk_size=BATCH_SIZE):
        task.delete()
    messages.error(request, 'All Task Deleted.')
    return redirect(homeView)
