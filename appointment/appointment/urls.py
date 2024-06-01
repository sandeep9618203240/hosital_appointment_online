from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',firstpage,name='firstpage'),
    path('accounts/', include('accounts.urls')),
    path('list/',list,name='list'),
    path('hospitals/',hospitals,name='hospitals'),
    # path('',firstpage,name='firstpage.html'),
    # path('accounts/', include('accounts.urls')),
 ]
