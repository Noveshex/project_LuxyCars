from django.contrib import admin
from .models import *


class CarsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price', 'status', 'is_published',)
    search_fields = ('brand', 'model',)
    list_filter = ('brand', 'model', 'status', 'is_published',)


admin.site.register(Status)
admin.site.register(Cars, CarsAdmin)

