from django.urls import path

from . import views


# creating path for the html files

urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name="index"),
    path("home.html", views.home, name="home"),
    path("store.html", views.store, name="store"),
    path("about.html", views.about, name="about"),
    path("add", views.add, name="add"),
    path("cart.html", views.cart, name="cart"),
    path("paym.html", views.paym, name="paym"),
    path("contact.html", views.contact, name="contact"),
    path("sign.html", views.register, name="register"),
    path("register", views.register, name="register"),
    path("login.html", views.login, name="login"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]
# name = "register"),
#     path("login", views.login, name="login"),
#     path("logout", views.logout, name="logout"),
# ]
