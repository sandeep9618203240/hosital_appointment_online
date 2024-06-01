from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if not User.objects.filter(username=username):
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            auth_login(request,user)
            return redirect('')
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/accounts/register/')
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created Successfully!")
        return redirect('/accounts/login/')
    return render(request,'register.html')