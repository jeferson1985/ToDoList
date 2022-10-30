from django.contrib import admin

from .models import Tasks

class TasksAdmin(admin.ModelAdmin):
    list_display = ['title', 'descriptions', 'status', 'date']
    list_filter = ['title', 'descriptions']
    search_filter = ['title']

admin.site.register(Tasks, TasksAdmin)
