from django.urls import path
from .views import *


urlpatterns = [
    path('', cars, name='home'),
    path('cars/<slug:car_brand>/', cars_categories, name='cars'),
    path('cars/orders', orders, name='orders'),
    path('cars/archive', archive, name='archive'),
]

