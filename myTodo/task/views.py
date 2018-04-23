from django.shortcuts import render
from django.template.response import TemplateResponse
from task.models import Task
#import pdb

def index(request):
    # Get tasks
    tasks = list(Task.objects.all())
    #pdb.set_trace()
    return TemplateResponse(request, 'myTodo/index.html',
                            {'tasks': tasks})
