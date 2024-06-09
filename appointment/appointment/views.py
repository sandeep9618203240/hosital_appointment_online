from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.models import Doctor,patient
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.
def hospitals(request):
    return render(request,'hospitals.html')
def firstpage(request):
    return render(request,'firstpage.html')
def bookappointment(request):
    return render(request,'bookappointment.html')
def trail(request):
    return render(request,'trail.html')
def doctors(request,username):
    query=Doctor.objects.get(username=username)
    set=patient.objects.filter(doctor=query)
    return render(request,'doctors.html')
def login_doc(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        x=Doctor.objects.filter(username=username)
        if not Doctor.objects.filter(username=username):
            print(username)
            messages.error(request, 'Invalid Username')
            return redirect('/login_doc/')
        # user=authenticate(username=username,password=password)
        if x is None:
            messages.error(request, "Invalid Password")
            return redirect('/login_doc/')
        else:
            # auth_login(request,user)
            query=Doctor.objects.get(username=username)
            return redirect(f'/doctors/{username}/')
    return render(request,'login.html')