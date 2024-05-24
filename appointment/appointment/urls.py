from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',list,name='list.html'),
    path('hospitals/',hospitals,name='hospitals.html'),
    path('',firstpage,name='firstpage.html')
 ]
