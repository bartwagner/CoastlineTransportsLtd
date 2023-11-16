from django.shortcuts import render, redirect
from .formsRegister import registerForm

def index(request):
    form = registerForm()
    return render(request, 'register/register.html', {'form': form})

def registerCostumer(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            return redirect('register')
        else:
            form = registerForm()
    return render(request, 'register.html', {'form': form})