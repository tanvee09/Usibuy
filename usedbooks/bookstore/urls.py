from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'bookstore-home'),
    path('buy/', views.buy, name = 'bookstore-buy'),
    path('sell/', views.sell, name = 'bookstore-sell'),
]
