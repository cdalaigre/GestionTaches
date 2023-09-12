
from django.utils.html import format_html
from datetime import datetime, date, timedelta
from django.db import models


# Create your models here.
class Task( models.Model ):
    name = models.CharField ( max_length =250)
    description = models.TextField ()
    creation_date = models.DateField (auto_now_add=True)
    due_date = models.DateField (null=True)
    schedule_date = models.DateField(default=datetime.now()+timedelta(days=7))
    closed = models.BooleanField (default = False)
        
    def __str__ (self):
        return self.name

    def colored_due_date (self):
        # definition de la variable color en fonction de la due_date
        
        if self.due_date is None or self.due_date - timedelta(days =7) > date.today():
            color = "green"
        elif self.due_date < date.today():
            color = "red"
        else:
            color = "orange"
        
        Mois=['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Decembre']
        jour = date.strftime(self.due_date,'%d')
        mois = int(date.strftime(self.due_date,'%m'))
        annee = date.strftime(self.due_date,'%Y')
        mois = Mois[mois-1]
        return format_html("<span style=color:%s>%s %s %s</span>" %(color,jour, mois, annee))

    colored_due_date.allow_tags = True