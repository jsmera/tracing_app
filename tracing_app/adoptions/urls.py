from django.urls import path

from .views import  AdopterListView, AdopterCreateView, AdopterUpdateView, TaskListView, TaskCreateView, TaskUpdateView

app_name = "adoptions"
urlpatterns = [
  
    path("adopters/", AdopterListView.as_view(), name='adopter-list'),
    path("adopters/new", AdopterCreateView.as_view(), name='adopter-new'),
    path("adopters/<int:pk>", AdopterUpdateView.as_view(), name="adopter-edit"),

    path("task/", TaskListView.as_view(), name='task-list'),
    path("task/new", TaskCreateView.as_view(), name="task-new"),
    path("task/<int:pk>", TaskUpdateView.as_view(), name="task-edit"),
]