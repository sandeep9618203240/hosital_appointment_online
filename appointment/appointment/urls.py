from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from accounts.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstpage/',firstpage,name='firstpage'),
    path('accounts/', include('accounts.urls')),
    path('hospitals/',hospitals,name='hospitals'),
    path('bookappointment/',bookappointment,name='bookappointment'),
    path('',trail,name='trail'),
    path('doctors/<username>/',doctors,name='doctors'),
    path('login_doc/',login_doc,name='login_doc')
 ]
