from django.template.response import TemplateResponse

def index(request):
    return TemplateResponse(request, 'myTodo/index.html')
