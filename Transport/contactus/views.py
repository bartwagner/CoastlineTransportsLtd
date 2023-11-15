from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django. contrib import messages
from .forms import contactUsForm

# Create your views here.
def index(request):
    form = contactUsForm()
    return render(request, 'contactus/contactus.html', {'form': form})

def email(request):
    form = contactUsForm(request.POST)
    if form.is_valid():
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        ticket = request.POST['ticket']
        message = request.POST['message']
        send_mail('New Question Costumer - ' + name, 
                'Ticket= ' + ticket + '\n' + 'Phone= ' + phone + '\n' + 'Message:'+ '\n' + message, 
                email, 
                ['info@discoverybus.ca']
        )
        messages.success(request, 'Thanks for your message ' + name +', We will be in contact soon')
        return redirect('contactus')
    messages.error(request, 'There was something wrong')
    return redirect('contactus')