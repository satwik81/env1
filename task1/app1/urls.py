from django.urls import path 
from . import views

urlpatterns = [
    path('',views.uploadfilecsv,name='home'),
    path('uploadsuccess/',views.uploadsuccess,name='success'),
]

