from django.urls import path
from . import views

urlpatterns =[
path('',views.contact,name='contact'),
path('detail/<cid>',views.detail,name='detail'),
]