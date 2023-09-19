from django.urls import path
from . import views

urlpatterns = [
    path('home/<param>',views.TellWelcomeToSomeOne ,name='welcome'),
    path('home',views.home ,name='home'),
    path('listing', views.task_listing, name="listing"),
    path('listing2', views.task_listing2, name="listing2"),
    path('listing3', views.task_listing3, name="listing3"),
    path('email/<pk>', views.email_detail, name="email"),
]
