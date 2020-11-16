from django.urls import path

from .views import   TaskListView, TaskCreateView, TaskUpdateView
#/<int:pk>/<int:pk2>
app_name = "tasks"
urlpatterns = [
    path("tasks/", TaskListView.as_view(), name='task-list'),
    path("tasks/new", TaskCreateView.as_view(), name="task-new"),
    path("tasks/<int:pk>", TaskUpdateView.as_view(), name="task-edit"),
]