from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'pages/index.html')

def register(request):
    if request.method == 'POST':
        messages.error(request, 'Testtttttttttttiiiinnnngggggggggggg')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def myaccount(request):
    return render(request, 'accounts/myaccount.html')