from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.discover, name='discover'),
    path('main', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts,name='contacts')
]
