from .models import *
from .forms import *

menu = [
            {'title': 'Main', 'url_name': 'main'},
            # {'title': 'About', 'url_name': 'about'},
            {'title': 'Cars', 'url_name': 'cars'},
            {'title': 'Contacts', 'url_name': 'contacts'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        status = Status.objects.all()
        cars = Cars.objects.all()
        contact_form = GetContactForm()
        register_form = RegisterUserForm()
        login_form = LoginUserForm()
        context['menu'] = menu
        context['status'] = status
        context['cars'] = cars
        context['contact_form'] = contact_form
        context['register_form'] = register_form
        context['login_form'] = login_form

        return context