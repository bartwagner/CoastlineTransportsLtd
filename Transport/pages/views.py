from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def faq(request):
    return render(request, 'pages/faq.html')

def safety(request):
    return render(request, 'pages/safety.html')

def shipping(request):
    return render(request, 'pages/shipping.html')

def charterBus(request):
    return render(request, 'pages/charterBus.html')