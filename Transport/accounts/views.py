from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'pages/index.html')

def register(request):
    if request.method == 'POST':

        # Get from values
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        confirm_email = request.POST['confirm_email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if password have 6 to 20 digits and another condicionals
        if len(password) >= 6 and len(password) <= 20 and password != '123456' and password != 'abcdef' and password != '654321' and password != first_name and password != last_name:
            if first_name != last_name:
                # Check if passwords match
                if password == confirm_password:
                    # Check if e-mails match
                    if email == confirm_email:
                        #Check username
                        if User.objects.filter(username=username).exists():
                            messages.error(request, 'That username is taken')
                            return redirect('register')    
                        else:
                            if User.objects.filter(email=email).exists():
                                messages.error(request, 'That email is being used')
                                return redirect('register')
                            else:
                                user = User.objects.create_user(username   = username,
                                                                first_name = first_name,
                                                                last_name  = last_name,
                                                                email      = email,
                                                                password   = password)
                                user.save()
                                messages.success(request, 'You are now registered and can log in')
                                return redirect('login')
                    else:
                        messages.error(request, 'E-mail do not match')
                        return redirect('register')
                else:
                    messages.error(request, 'Passwords do not match')
                    return redirect('register')
            else:
                messages.error(request, 'First Name can not be the same as the Last Name')
                return redirect('register')
        else:
            messages.error(request, 'The password needs to have six digits or It does not meet the criteria')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def myaccount(request):
    return render(request, 'accounts/myaccount.html')