from django.urls import path
from .views import *


urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('about/', AboutView.as_view(), name='about'),
    path('cars/', CarsListView.as_view(), name='cars'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('cars/<slug:status_slug>/list/', CarsStatusList.as_view(), name='cars_status_list'),
    path('cars/<slug:car_slug>/', ShowCar.as_view(), name='car'),
]

