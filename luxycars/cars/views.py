from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def cars(request):
    return HttpResponse('Cars')


def cars_categories(request, car_brand):
    return HttpResponse(f'<h1>Cars Categories</h1><p>{car_brand}</p>')


sold = {
    "brand": "model"
}


def archive(request, car):
    if car in sold:
        return redirect('orders')


def orders(request):
    return HttpResponse(f'<h1>Orders Page</h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Not Found</h1>')