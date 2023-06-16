from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from .utils import menu
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .utils import *
from .forms import UserUpdateForm


class Main(DataMixin, ListView):
    model = Cars
    template_name = 'cars/base.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Luxy Cars')

        return dict(list(context.items()) + list(c_def.items()))


# class AboutView(DataMixin, ListView):
#     model = Status
#     template_name = 'cars/about.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='About Us')
#
#         return dict(list(context.items()) + list(c_def.items()))


class ContactView(DataMixin, CreateView):
    form_class = GetContactForm
    template_name = 'cars/contacts.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Contact Us')

        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'cars/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Registration')

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('main')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'cars/login.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Authentication')

        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    try:
        if request.method == 'POST':
            update_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        else:
            update_form = UserUpdateForm(request.POST, instance=request.user)

        if update_form.is_valid():
            update_form.save()
            return redirect('profile')

        user = User.objects.get(id=request.user.id)
        title = user.username

        context = {
            'user': user,
            'title': title,
            'menu': menu,
            'update_form': update_form,
        }
        return render(request, 'cars/profile.html', context=context)
    except ObjectDoesNotExist:
        pass


# class CarsStatusList(DataMixin, ListView):
#     model = Status
#     template_name = 'cars/cars_status_list.html'
#     context_object_name = 'cars'
#     allow_empty = False
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Luxy ' + str(context['cars'][0].status) + ' Cars')
#
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def get_queryset(self):
#         return Cars.objects.filter(status__slug=self.kwargs['status_slug'], is_published=True)


class CarsListView(DataMixin, ListView):
    paginate_by = 4
    model = Cars
    template_name = 'cars/cars.html'
    context_object_name = 'object_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Luxy Cars')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Cars.objects.filter(is_published=True).select_related('status')


def cars_status_list(request, status_slug):
    status = Status.objects.get(slug=status_slug)
    cars = Cars.objects.filter(status=status)
    title = "Luxy " + status.status + " Cars"

    context = {
        'cars': cars,
        'status': status,
        'title': title,
        'menu': menu,
    }

    return render(request, 'cars/cars_status_list.html', context=context)


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


class ProcessOrder(DataMixin, DetailView):
    model = Cars
    template_name = 'cars/order.html'
    slug_url_kwarg = 'car_slug'
    context_object_name = 'car'

    def post(self, request, *args, **kwargs):
        car = self.get_object()
        # Дополните эту часть кода логикой обработки заказа, например, созданием объекта заказа в базе данных или отправкой уведомления.

        # После обработки заказа, перенаправьте пользователя на страницу успешного оформления заказа.
        return redirect('order_success')


def order_success(request):
    return render(request, 'cars/order_success.html')

