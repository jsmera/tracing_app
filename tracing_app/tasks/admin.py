from django.contrib import admin
from .models import Task
from .forms import  CreateTaskForm


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    form = CreateTaskForm
    add_form = CreateTaskForm
    list_display = ["date", "status", "date_end","adopcion"]
    search_fields = ["date","date_end"]
