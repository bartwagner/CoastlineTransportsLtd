from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def register(request):
    return render(request, 'pages/register.html')

def login(request):
    return render(request, 'pages/login.html')

def faq(request):
    return render(request, 'pages/faq.html')

def safety(request):
    return render(request, 'pages/safety.html')

def shipping(request):
    return render(request, 'pages/shipping.html')

def charterBus(request):
    return render(request, 'pages/charterBus.html')

def tickets(request):
    return render(request, 'pages/tickets.html')

def schedules(request):
    return render(request, 'pages/schedules.html')

def bookTrip(request):
    return render(request, 'pages/bookTrip.html')

def contactUs(request):
    return render(request, 'pages/contactUs.html')






def loyaltyRegister(request):
    return render(request, 'pages/loyaltyRegister.html')

def privacyPolicy(request):
    return render(request, 'pages/privacyPolicy.html')

def termsConditions(request):
    return render(request, 'pages/termsConditions.html')

def cancelChangesReserve(request):
    return render(request, 'pages/cancelChangesReserve.html')