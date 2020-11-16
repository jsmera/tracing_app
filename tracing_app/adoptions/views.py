from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse 
from .models import  Adoption
from .forms import  CreateAdoptionForm


class AdoptionListView(ListView):
    model = Adoption
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AdoptionCreateView(CreateView):
    model = Adoption
    form_class = CreateAdoptionForm
    def get_success_url(self):
        return reverse("adoptions:adoption-list")

class AdoptionUpdateView(UpdateView):
    model = Adoption
    form_class = CreateAdoptionForm
    def get_success_url(self):
        return reverse("adoptions:adoption-list")
