from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse 
from .models import  Task
from .forms import  CreateTaskForm



class TaskListView(ListView):
    model = Task
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TaskCreateView(CreateView):
    model = Task
    form_class = CreateTaskForm
    def get_success_url(self):
        return reverse("tasks:task-list")

class TaskUpdateView(UpdateView):
    model = Task
    form_class = CreateTaskForm
    def get_success_url(self):
        return reverse("tasks:task-list")
