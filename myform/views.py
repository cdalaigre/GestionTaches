from django.shortcuts import render,redirect
from django.forms import ModelForm, Textarea
from myform.models import Contact
from django import forms
from django.forms.fields import DateField,ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect,CheckboxSelectMultiple,SelectDateWidget,Textarea
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

# Avec ModelForm
class ContactForm ( ModelForm ):
    
    def __init__ (self, *args, ** kwargs):
        super( ContactForm, self). __init__ (*args , ** kwargs)
        self.fields['name'].label = "Nom"
        self.fields['firstname'].label = " Prenom"
        self.fields['email'].label = "courriel"

    class Meta:
        model = Contact
        fields = ('name', 'firstname', 'email', 'message')
        widgets = {'message': Textarea(attrs ={'cols':60,'rows':10}),}

# Sans ModelForm
class ContactForm2 (forms.Form):
    name = forms.CharField (max_length=200,initial="votre nom",label ="nom")
    firstname = forms.CharField(max_length =200,initial="votre prenom",label ="prenom")
    email = forms.EmailField(max_length=200, label="courriel")
    message = forms.CharField(widget=forms.Textarea (attrs = { 'cols':60, 'rows':10}) )

class CommentForm ( forms.Form):
    name = forms.CharField (widget = forms.TextInput(attrs ={ 'class':'special'}))
    url = forms.URLField ()
    comment = forms. CharField (widget = forms.TextInput ( attrs ={ 'size':'40'}))

BIRTH_YEAR_CHOICES = ('1999 ', '2000 ', '2001 ')
GENDER_CHOICES = (( 'm', 'Male '), ('f', 'Female '))
FAVORITE_COLORS_CHOICES = (( 'blue ', 'Blue '),('green ', 'Green '),('black ', 'Black '))

class SimpleForm (forms.Form):
    birth_year = DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    gender = ChoiceField(widget=RadioSelect,choices=GENDER_CHOICES )
    favorite_colors = forms.MultipleChoiceField(required=False, widget=CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES )

def contact ( request ):
    form = ContactForm()
    # on teste si on est bien en validation de formulaire (POST)
    if request.method == "POST":
        # Si oui on récupère les données postées
        form = ContactForm(request.POST)
        # on vérifie la validité du formulaire
        if form.is_valid():
            new_contact = form.save()
            # on prépare un nouveau message
            messages.success(request ,'Nouveau contact '+ new_contact.name +' '+ new_contact.email )
            # return redirect ( reverse (' detail ', args =[ new_contact .pk] ))
            context = {'pers': new_contact, 'messages': messages }
            return render (request,'detail.html', context)
        
    context = {'form': form}
    return render (request ,'contact.html', context)
    #contact_form2 = ContactForm2()
    #comment_form = CommentForm(auto_id=False)
    #simple_form = SimpleForm()
    #return render (request ,'contact.html', {'contact_form':contact_form,'contact_form2':contact_form2,'comment_form':comment_form,'simple_form':simple_form })

def detail (request, cid):
    contact = Contact.objects.get(pk=cid)
    return HttpResponse('Nouveau contact '+ contact.name+' '+ contact.email )