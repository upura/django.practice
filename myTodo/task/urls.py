from django.conf.urls import url
from django.contrib import admin

import task.views

urlpatterns = [
    url(r'^task/new/$', task.views.task_new, name='task_new'),
    url(r'^$', task.views.index, name='index'),
    url(r'^task/(?P<task_id>[0-9]+)$', task.views.task_detail, name='task_detail'),
    url(r'^task/(?P<task_id>[0-9]+)/delete$', task.views.task_delete, name='task_delete'),
]
