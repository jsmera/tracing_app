from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from tracing_app.tasks.models import Task
from tracing_app.tasks.tasks import create_tasks
from .models import Adoption
from .forms import CreateAdoptionForm, EditAdoptionForm
from django.contrib.auth.mixins import LoginRequiredMixin


class AdoptionListView(LoginRequiredMixin, ListView):
    model = Adoption

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AdoptionCreateView(LoginRequiredMixin, CreateView):
    model = Adoption
    form_class = CreateAdoptionForm

    def get_success_url(self):
        return reverse("adoptions:adoption-list")

    def form_valid(self, form):
        url = super(AdoptionCreateView, self).form_valid(form)
        create_tasks.apply((self.object.id,))
        return url


class AdoptionUpdateView(LoginRequiredMixin, UpdateView):
    model = Adoption
    form_class = EditAdoptionForm

    def get_success_url(self):
        return reverse("adoptions:adoption-list")

    def get_context_data(self, **kwargs):
        context = super(AdoptionUpdateView, self).get_context_data(**kwargs)
        context["task_list"] = (
            Task.objects.filter(
                adopcion=self.object,
            )
            .exclude(status__in=["canceled"])
            .order_by("date_start")
        )

        return context
