from django.shortcuts import render
from django.http import HttpResponse
from GestionTaches.settings import STATIC_URL
from lesTaches.models import Email, Task 
from django.template import Template , Context

# Create your views here.
def TellWelcomeToSomeOne( request, param ):
    return HttpResponse ('bonjour à ' + param + " depuis mon serveur DJANGO")

def home( request ):
    return HttpResponse ("Bonjour à tous ! Bienvenus sur la page d'accueil de mon serveur DJANGO")


def task_listing ( request ):
    objets =Task.objects.all().order_by('due_date')
    return render (request, template_name ='list.html',context={'objets':objets})

def task_listing2 ( request ):
    objets =Task. objects.all().order_by('due_date')
    #print ( objets )
    # - ( inverse l'ordre )
    return render (request , template_name ='list2.html',context={'taches':objets})

def task_listing3 ( request ):
    objects = Task.objects.all().order_by('due_date')
    return render (request , template_name ='list3.html', context ={'objects': objects} )

def email_detail(request, pk):
    email = Email.objects.get(pk=pk)
    user = email.user
    listes_abonnees = email.listes.all()
    template = 'email_detail.html'
    context = {'user': user, 'email': email.mail, 'listes': listes_abonnees }
    return render(request, template, context)