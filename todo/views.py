from django.shortcuts import render, redirect
from .forms import TodoCreationForm
from .models import Todo
# Create your views here.
def index(request):
    title = 'Todo'
    todo = Todo.objects.all()
    if request.method != 'POST':
        form = TodoCreationForm()
    else:
        form = TodoCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
    context = {
        'title': title,
        'form': form,
        'todos': todo,
    }
    return render(request, 'todo/index.html', context)

def delete_todo(request):
    if request.method == 'POST':
        todo_id = request.POST.get('todo_id')
        Todo.objects.filter(id=todo_id).delete()
    return redirect('todo:index')