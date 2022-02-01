from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from twilio.rest import Client
from random import randint
from .models import Account

otp = randint(1000, 9999)


def testing(request):
    if request.method == 'POST':
        send1 = request.POST['send1']
        username = request.POST['username']
        if send1:
            send_authentication(send1)
            return render(request, 'testing2.html', {'phone': send1, 'username': username})
    return render(request, 'testing.html')


def testing2(request):
    if request.method == 'POST':
        send2 = request.POST['send2']
        username = request.POST['username']

        if int(send2) == otp:
            messages.success(request, 'success')
            user = User.objects.get(username=username)
            user.is_active = True
            user.save()
            return render(request, 'login.html')
        else:
            messages.success(request, 'Fail')
    return render(request, 'testing2.html', {'send2': send2})


def resend(request):
    messages.success(request, 'ok')
    return render(request, 'testing.html')


def index(request):
    return render(request, 'index.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            name = user.username
            return render(request, 'index.html', {'name': name})
        else:
            ac = User.objects.all()
            test1 = User.objects.get(username=username)

            if test1.is_active is False:
                return render(request, 'testing.html', {'username': username})

            messages.error(request, f'Username and password are not match ')
            return render(request, 'login.html')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username):
            messages.error(request, 'Username is already exist.')

        users = User.objects.create_user(username, email, password)
        users.is_active = False
        users.save()

        messages.success(request, 'Ok')
        return render(request, 'index.html')

    return render(request, 'signup.html')


def sign_out(request):
    logout(request)
    messages.success(request, 'Logged out success')
    return redirect('home')


def send_authentication(request):
    account_sid = 'ACb91498c34992a56f7224ee3e749d1565'
    token_id = '68287c0eb97e5e09ae70d71b0074794e'
    otp_client = Client(account_sid, token_id)
    otp_messages = otp_client.messages.create(
        body=f'OTP: {otp}',
        from_='+13866741924',
        to=f'+63{request}'
    )


def send_otp(request):
    if request.method == 'POST':
        otp_verified = request.POST['otp_verified']
        user = User.objects.all()
        if int(otp_verified) == otp:
            messages.success(request, 'Verification successfully')
            return render(request, 'login.html')
        else:
            messages.success(request, 'OTP not match')

    return render(request, 'user_authenticate.html')
