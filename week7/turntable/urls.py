from django.urls import path
from . import views


app_name = 'turntable'
urlpatterns = [
    # ex: /turntable/
    path('', views.index, name='index'),
    path('', views.thank_you_1, name='thank_you_1'),
    path('', views.turntable, name='turntable'),
    # ex: /turntable/phone_check
    path('phone_check', views.phone_check, name='phone_check'),

]
