from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import Http404
from task.models import Task
import pdb
def index(request):
    tasks = list(Task.objects.all())
    return TemplateResponse(request, 'task/index.html',
                            {'tasks': tasks})

def task_detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
#        pdb.set_trace()
    except Task.DoesNotExist:
        raise Http404
    return TemplateResponse(request, 'task/task_detail.html',
                            {'task': task})
