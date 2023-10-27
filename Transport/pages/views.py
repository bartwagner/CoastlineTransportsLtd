from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def safety(request):
    return render(request, 'pages/safety.html')

def schedules(request):
    return render(request, 'pages/schedules.html')

def fares(request):
    return render(request, 'pages/fares.html')

def faq(request):
    return render(request, 'pages/faq.html')

def busCharters(request):
    return render(request, 'pages/busCharters.html')

def boxByBus(request):
    return render(request, 'pages/boxByBus.html')