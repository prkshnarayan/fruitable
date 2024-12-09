from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def shop(request):
    return render(request, 'shop.html')


def shop_detail(request):
    return render(request, 'shop-detail.html')


def cart(request):
    return render(request, 'cart.html')


def chackout(request):
    return render(request, 'chackout.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def error404(request):
    return render(request, '404.html')


def contact(request):
    return render(request, 'contact.html')
