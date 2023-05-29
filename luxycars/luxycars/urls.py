from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from cars.views import *
from luxycars import settings

urlpatterns = [
    path('', include('cars.urls')),
    path('admin/', admin.site.urls, name='admin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
