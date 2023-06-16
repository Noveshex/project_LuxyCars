from django.urls import path
from django.views.decorators.cache import cache_page
from django.contrib.auth import views as authViews

from .views import *


urlpatterns = [
    path('', Main.as_view(), name='main'),
    # path('about/', AboutView.as_view(), name='about'),
    path('cars/', CarsListView.as_view(), name='cars'),
    path('cars/<slug:status_slug>/list/', cars_status_list, name='cars_status_list'),
    path('cars/<slug:car_slug>/', ShowCar.as_view(), name='car'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('pass-reset/', authViews.PasswordResetView.as_view(template_name='cars/pass_reset.html'), name='pass-reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         authViews.PasswordResetConfirmView.as_view(template_name='cars/pass_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-done/', authViews.PasswordResetDoneView.as_view(template_name='cars/pass_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-complete/',
         authViews.PasswordResetCompleteView.as_view(template_name='cars/pass_reset_complete.html'),
         name='password_reset_complete'),
    path('cars/<slug:car_slug>/order/', ProcessOrder.as_view(), name='process_order'),
    path('order-success/', order_success, name='order_success'),
]

