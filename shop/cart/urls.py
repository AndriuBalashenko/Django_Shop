from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('order/', views.view_order, name='order'),
    path('add/', views.add_to_cart, name='add_to_cart',),
    path('remove/', views.cart_remove, name = 'remove'),
    path('', views.view_cart, name='cart',),
]
