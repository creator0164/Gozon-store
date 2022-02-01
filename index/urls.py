from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.sign_in),
    path('signup/', views.signup),
    path('logout/', views.sign_out),
    path('send/', views.send_authentication),
    path('send_otp/', views.send_otp),
    path('testing/', views.testing),
    path('testing2/', views.testing2),
    path('resend/', views.resend)
]
