from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from .models import Pet
from .forms import CreatePetForm
from django.contrib.auth.mixins import LoginRequiredMixin


class PetListView(LoginRequiredMixin, ListView):
    model = Pet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "hello"
        return context


class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = CreatePetForm

    def get_success_url(self):
        return reverse("pets:pets-list")


class PetUpdateView(LoginRequiredMixin, UpdateView):
    model = Pet
    form_class = CreatePetForm

    def get_success_url(self):
        return reverse("pets:pets-list")
