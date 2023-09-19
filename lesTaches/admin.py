from django.contrib import admin
from lesTaches.models import Email, ListeDiffusion, Task, Utilisateur

# Register your models here.

class TaskAdmin ( admin.ModelAdmin ):
    list_display =('name', 'description', 'creation_date', 'schedule_date', 'colored_due_date', 'closed')

class UtilisateurAdmin ( admin.ModelAdmin ):
    list_display =('id','nom')

class EmailAdmin ( admin.ModelAdmin ):
    list_display =('id','mail','user')

class ListeDiffusionAdmin ( admin.ModelAdmin ):
    list_display =('id','listeName')
    
admin.site.register (Task , TaskAdmin)
admin.site.register (Utilisateur , UtilisateurAdmin)
admin.site.register (Email , EmailAdmin)
admin.site.register (ListeDiffusion , ListeDiffusionAdmin)