from django.urls import path

from .views import PetsListView, PetCreateView, PetUpdateView

app_name = "adoptions"
urlpatterns = [
    path("pets/", PetsListView.as_view(), name='pet-list'),
    path("pets/new", PetCreateView.as_view(), name="pet-new"),
    path("pets/<int:pk>", PetUpdateView.as_view(), name="pet-edit"),
]