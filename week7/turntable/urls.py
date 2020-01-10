from django.urls import path
from . import  views

app_name = 'turntable'
urlpatterns = [
    # ex: /turntable/
    path('', views.index, name='index'),
    path('phoneno', views.phoneno, name='phoneno'),
    path('prize.html',views.prizes, name='prize'),
    path('no_prize.html',views.no_prizes,name='no_prize')

]
