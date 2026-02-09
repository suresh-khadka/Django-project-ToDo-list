from django.http import HttpResponse
from django.shortcuts import render
from todos.models import Task


def home(request):
    task= Task.objects.filter(Is_completed=False).order_by("-Updated_at")
    not_com_task= Task.objects.filter(Is_completed=True)
    return render(request , "home.html" , {'task' : task , 'not_com_task' : not_com_task})

