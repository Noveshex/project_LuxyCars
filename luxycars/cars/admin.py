from django.contrib import admin
from .models import *


class CarsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price', 'status', 'is_published',)
    search_fields = ('brand', 'model',)
    list_filter = ('brand', 'model', 'status', 'is_published',)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'is_answered',)
    list_filter = ('time', 'is_answered',)


admin.site.register(Status)
admin.site.register(Cars, CarsAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
