from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from .models import Adopter
from .forms import CreateAdopterForm


class AdopterListView(ListView):
    model = Adopter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AdopterCreateView(CreateView):
    model = Adopter
    form_class = CreateAdopterForm

    def get_success_url(self):
        return reverse("adopters:adopter-list")


class AdopterUpdateView(UpdateView):
    model = Adopter
    form_class = CreateAdopterForm

    def get_success_url(self):
        return reverse("adopters:adopter-list")
