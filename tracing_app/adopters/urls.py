from django.urls import path

from .views import AdopterListView, AdopterCreateView, AdopterUpdateView

app_name = "adopters"
urlpatterns = [
    path("adopters/", AdopterListView.as_view(), name="adopter-list"),
    path("adopters/new", AdopterCreateView.as_view(), name="adopter-new"),
    path("adopters/<int:pk>", AdopterUpdateView.as_view(), name="adopter-edit"),
]
