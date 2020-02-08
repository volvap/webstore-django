from django.urls import path
from .views import item_list

from . import views


urlpatterns = [
    path('shop',views.item_list,name='item_list'),
    path('cart/<int:pk>', views.add_to_cart,name='add_to_cart'),
    path('delete/', views.delete_all_from_cart,name='delete_all_from_cart'),
    path('cart', views.display_cart,name='display_cart')

]
