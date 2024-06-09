from django.db import models
from .models import Doctor
from django.shortcuts import render, redirect
class first(models.Model):
    name=models.CharField(max_length=20)
    phonenumber=models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
# def doctors(request):
#     queryset = Doctor.objects.all()
#     context = {'doctors': queryset}
#     return render(request, 'doctors.html', context)
