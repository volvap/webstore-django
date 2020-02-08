from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name="logout_view"),
    path('log', views.my_view, name='my_view')
    ]
