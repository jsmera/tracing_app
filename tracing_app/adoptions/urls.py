from django.urls import path

from .views import   TaskListView, TaskCreateView, TaskUpdateView

app_name = "adoptions"
urlpatterns = [
  
    path("task/", TaskListView.as_view(), name='task-list'),
    path("task/new", TaskCreateView.as_view(), name="task-new"),
    path("task/<int:pk>", TaskUpdateView.as_view(), name="task-edit"),
]