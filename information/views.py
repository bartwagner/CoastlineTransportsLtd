from django.shortcuts import render

def termsconditions(request):
    return render(request, 'information/termsconditions.html')

def privacypolicy(request):
    return render(request, 'information/privacypolicy.html')

def faq(request):
    return render(request, 'information/faq.html')

def safety(request):
    return render(request, 'information/safety.html')

def schedules(request):
    return render(request, 'information/schedules.html')

def tickets(request):
    return render(request, 'information/tickets.html')