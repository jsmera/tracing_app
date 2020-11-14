from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse 
from .models import Adopter, Task
from .forms import  CreateAdopterForm, CreateTaskForm



class AdopterListView(ListView):
    model = Adopter
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AdopterCreateView(CreateView):
    model = Adopter
    form_class = CreateAdopterForm
    def get_success_url(self):
        return reverse("adoptions:adopter-list")

class AdopterUpdateView(UpdateView):
    model = Adopter
    form_class = CreateAdopterForm
    def get_success_url(self):
        return reverse("adoptions:adopter-list")



class TaskListView(ListView):
    model = Task
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TaskCreateView(CreateView):
    model = Task
    form_class = CreateTaskForm
    def get_success_url(self):
        return reverse("adoptions:task-list")

class TaskUpdateView(UpdateView):
    model = Task
    form_class = CreateTaskForm
    def get_success_url(self):
        return reverse("adoptions:task-list")
