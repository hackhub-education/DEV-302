from django.urls import path
from . import  views

app_name = 'turntable'
urlpatterns = [
    # ex: /turntable/
    path('', views.index, name='index'),
    path('phoneno', views.phoneno, name='phoneno'),

   


]
