from django.template.response import TemplateResponse
from django.http import Http404
from task.models import Task
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from task.forms import TaskEditForm
# from django.shortcuts import render


def index(request):
    tasks = list(Task.objects.all())
    return TemplateResponse(request, 'task/index.html',
                            {'tasks': tasks})


def task_detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = TaskEditForm(instance=task)

    return TemplateResponse(request, 'task/task_detail.html',
                            {'form': form, 'task': task})


def task_new(request):

    if request.method == 'POST':
        form = TaskEditForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = TaskEditForm()

    return TemplateResponse(request, 'task/task_new.html',
                            {'form': form})


def task_delete(request, task_id):
    if request.method == 'POST':
        try:
            Task.objects.get(id=task_id).delete()
            return HttpResponseRedirect(reverse('index'))
        except Task.DoesNotExist:
            raise Http404
    return TemplateResponse(request, 'task/index.html')
