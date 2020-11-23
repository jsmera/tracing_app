from django.urls import path

from .views import (
    TaskCreateView,
    TaskUpdateView,
    CompleteTaskView,
    DoneTaskView,
    ReminderCreateView,
    NotifyView,
    ConfigurationsListView,
    ConfigurationTaskCreateView,
    ConfigurationReminderCreateView,
    ConfigurationsUpdateView,
)

app_name = "tasks"
urlpatterns = [
    path("tasks/<int:adpotion>/new", TaskCreateView.as_view(), name="task-new"),
    path(
        "reminder/<int:adpotion>/new", ReminderCreateView.as_view(), name="reminder-new"
    ),
    path("tasks/<int:adpotion>/<int:pk>", TaskUpdateView.as_view(), name="task-edit"),
    path("notify/<int:task>", NotifyView.as_view(), name="task-notify"),
    path("t/<uuid:uuid>", CompleteTaskView.as_view(), name="public-task"),
    path("t/done", DoneTaskView.as_view(), name="done-task"),
    path("configurations/", ConfigurationsListView.as_view(), name="config-list"),
    path("reminders/new", ConfigurationReminderCreateView.as_view(), name="remin-new"),
    path(
        "configurations/new", ConfigurationTaskCreateView.as_view(), name="config-new"
    ),
    path(
        "configurations/<int:pk>",
        ConfigurationsUpdateView.as_view(),
        name="config-edit",
    ),
]
