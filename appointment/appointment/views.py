from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def list(request):
    return render(request,"list.html")
def hospitals(request):
    return render(request,'hospitals.html')
def firstpage(request):
    return render(request,'firstpage.html')
