from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import *
from .utils import *


class Main(DataMixin, ListView):
    model = Cars
    template_name = 'cars/base.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Luxy Cars')

        return dict(list(context.items()) + list(c_def.items()))


class AboutView(DataMixin, ListView):
    model = Status
    template_name = 'cars/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='About Us')

        return dict(list(context.items()) + list(c_def.items()))


class CarsListView(DataMixin, ListView):
    model = Cars
    template_name = 'cars/cars.html'
    context_object_name = 'cars'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Luxy Cars')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Cars.objects.filter(is_published=True)


class ContactView(DataMixin, ListView):
    model = Status
    template_name = 'cars/contacts.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Contact Us')

        return dict(list(context.items()) + list(c_def.items()))


class CarsStatusList(DataMixin, ListView):
    model = Status
    template_name = 'cars/cars_status_list.html'
    context_object_name = 'cars'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Luxy ' + str(context['cars'][0].status) + ' Cars')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Cars.objects.filter(status__slug=self.kwargs['status_slug'], is_published=True)


class ShowCar(DataMixin, DetailView):
    model = Cars
    template_name = 'cars/car.html'
    slug_url_kwarg = 'car_slug'
    context_object_name = 'cars'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['cars'].brand + " " + context['cars'].model

        return context


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Not Found</h1>')