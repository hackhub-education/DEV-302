from django.urls import path
from . import views


app_name = 'turntable'
urlpatterns = [
    # ex: /turntable/
    path('', views.index, name='index'),
    path('start', views.start, name='start'),
    path('reward', views.reward, name='reward')
]
