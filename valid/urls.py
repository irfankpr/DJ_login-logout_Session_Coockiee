from django.urls import path, include

from valid import views

# valid . urls

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('home', views.home),
    path('signout', views.signout)
]
