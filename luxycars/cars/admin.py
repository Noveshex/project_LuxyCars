from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CarsAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'price', 'status', 'get_img', 'is_published',)
    search_fields = ('brand', 'model',)
    list_filter = ('brand', 'model', 'status', 'is_published',)
    fields = ('slug', 'brand', 'model', 'type', 'year', 'price', 'about', 'images', 'get_img', 'rating', 'status', 'other', 'is_published')
    readonly_fields = ('get_img',)
    save_on_top = True

    def get_img(self, object):
        if object.images:
            return mark_safe(f"<img src='{object.images.url}' width=50>")

    get_img.short_description = "img"


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'is_answered',)
    list_filter = ('time', 'is_answered',)


admin.site.register(Status)
admin.site.register(Cars, CarsAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
