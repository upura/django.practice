from django import forms
from task.models import Task

class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'name',
            'text',
            'created_at'
        )
