from django.urls import path

from .views import PetListView, PetCreateView, PetUpdateView

app_name = "pets"
urlpatterns = [
    path("pets/", PetListView.as_view(), name="pets-list"),
    path("pets/new", PetCreateView.as_view(), name="pets-new"),
    path("pets/<int:pk>", PetUpdateView.as_view(), name="pets-edit"),
]
