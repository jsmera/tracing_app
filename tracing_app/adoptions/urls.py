from django.urls import path

from .views import AdoptionListView, AdoptionCreateView, AdoptionUpdateView

app_name = "adoptions"
urlpatterns = [
    path("adoptions/", AdoptionListView.as_view(), name="adoption-list"),
    path("adoptions/new", AdoptionCreateView.as_view(), name="adoption-new"),
    path("adoptions/<int:pk>", AdoptionUpdateView.as_view(), name="adoption-edit"),
]
