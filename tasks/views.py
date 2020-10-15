from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

    return render(request, 'tasks/lists.html', {
        'tasks': tasks, 'form': form
    })


def update_task(request, id):
    task = Task.objects.get(pk=id)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

    return render(request, 'tasks/update.html', {
        'form': form
    })


def delete_task(request, id):
    item = Task.objects.get(pk=id)

    if request.method == 'POST':
        item.delete()
        return HttpResponseRedirect('/')
    return render(request, 'tasks/delete.html', {
        'item': item
    })

