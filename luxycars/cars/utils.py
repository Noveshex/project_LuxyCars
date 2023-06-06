from .models import *

menu = [
            {'title': 'Main', 'url_name': 'main'},
            {'title': 'About', 'url_name': 'about'},
            {'title': 'Cars', 'url_name': 'cars'},
            {'title': 'Contacts', 'url_name': 'contacts'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        status = Status.objects.all()
        cars = Cars.objects.all()
        context['menu'] = menu
        context['status'] = status
        context['cars'] = cars

        return context