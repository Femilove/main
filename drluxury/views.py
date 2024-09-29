from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *

# Create your views here.

# creating a fuction for login.url so it can be called by index.html


def index(response):
    return render(response, 'index.html')

# creating a fuction for home.url


def home(response):
    return render(response, 'home.html')


def cart(response):
    return render(response, 'cart.html')


def paym(response):
    return render(response, 'paym.html')


def add(response):

    # POST is used to give info to the user without the info spreading in the search bar
    # GET is used to get info from the user which display the info on the search bar

    val1 = (response.POST['num1'])

    res = val1

    return render(response, 'cart.html', {"result": res,
                                          })

# creating a fuction for store.url


def store(response):
    dests = Destination.objects.all()
    dests1 = Destination2.objects.all()
    dests2 = Destination3.objects.all()
    dests3 = Destination4.objects.all()
    dests4 = Destination5.objects.all()
    dests5 = Destination6.objects.all()
    dests6 = Destination7.objects.all()
    return render(response, 'store.html', {'dests': dests,
                                           'dests1': dests1,
                                           'dests2': dests2,
                                           'dests3': dests3,
                                           'dests4': dests4,
                                           'dests5': dests5,
                                           'dests6': dests6})

# creating a fuction for contact.url


def contact(response):
    return render(response, 'contact.html')

# creating a fuction for about.url


def about(response):
    return render(response, 'about.html')

# creating a fuction for register.url


def register(response):

    if response.method == 'POST':
        first_name = response.POST['first_name']
        last_name = response.POST['last_name']
        username = response.POST['username']
        password1 = response.POST['password1']
        password2 = response.POST['password2']
        email = response.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(response, 'Username Taken')
                return redirect('register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(response, 'Email Taken')
                return redirect('register.html')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user Created')
                return redirect('login.html')
        else:
            messages.info(response, 'Password not matching')
            return redirect('register.html')

    else:
        return render(response, 'register.html')

# creating a fuction for login.url


def login(response):
    if response.method == 'POST':
        username = response.POST['username']
        password = response.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(response, user)
            return redirect("home.html")
        else:
            messages.info(response, 'Invaliid credencials')
            return redirect("login.html")

    else:
        return render(response, 'login.html')

# creating a fuction for logout.url


def logout(response):
    auth.logout(response)
    return redirect('/')
