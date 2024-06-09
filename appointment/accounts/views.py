from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Doctor,patient
from django.contrib import messages

def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username):
            print(username)
            messages.error(request, 'Invalid Username')
            return redirect('/accounts/login/')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/accounts/login/')
        else:
            auth_login(request,user)
            return redirect('/bookappointment/')
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

def bookappointment(request):
    ueryset=Doctor.objects.all()
    list=[]
    for i in ueryset:
        list.append(i.designation)
    context = {'list':list}
    print(context)
    
    if request.method=="POST":

        name = request.POST.get('nameid', '')
        sur_name= request.POST.get('sur_name', '')
        age= request.POST.get('age', '')
        address= request.POST.get('address', '')
        phone= request.POST.get('phone', '')
        disease_dis=request.POST.get('disease_dis', '')
        date= request.POST.get('date', '')
        doctor= request.POST.get('doctor', '')


        queryset=Doctor.objects.get(designation=doctor)
        print(queryset)
        patient.objects.create(
            name = name,
            sur_name=sur_name,
            age=age,
            address=address,
            phone=phone,
            disease_dis=disease_dis,
            date=date,
            doctor=queryset
        )
        messages.success(request, "your appointment is success") 
        return redirect ('/bookappointment/')
        
    
    return render(request,'bookappointment.html',context)


    