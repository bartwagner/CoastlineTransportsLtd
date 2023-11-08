from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django. contrib import messages

# Create your views here.
def index(request):
    return render(request, 'contactus/contactus.html')

def email(request):
    send_mail('Assunto', 'Teste de envio', 'bart_wagner_g@hotmail.com', ['bart_wagner_g@hotmail.com'])

    messages.success(request, 'Thanks for your message')
    return redirect('contactus')