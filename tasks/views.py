from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from tasks.models import Todo

# Create your views here.

def index(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, "main/index.html", {
        "todo_items":todo_items
    })

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = Todo.objects.create(added_date=current_date, text=content)
    lenght_of_todos = Todo.objects.all().count()
    return HttpResponseRedirect("/")


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
    
    