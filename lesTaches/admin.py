from django.contrib import admin
from lesTaches.models import Task

# Register your models here.

class TaskAdmin ( admin.ModelAdmin ):
    list_display =('name', 'description', 'creation_date', 'schedule_date', 'colored_due_date', 'closed')
    
admin.site.register (Task , TaskAdmin)