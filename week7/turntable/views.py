from django.shortcuts import render, get_object_or_404
import random

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from django.urls import reverse

from .models import Prizes,User


def index(request):
    
    return render(request, 'turntable/index.html')

    

def phoneno(request):
    prize_list = Prizes.objects.order_by('-amount')
    base = 1000
    amount = random.randint(0,999)
    difference = base - amount
    if difference > 0 and  difference == 1:
        prize_id = 1
    
    elif difference > 0 and  difference == 2:
         prize_id = 2

    elif difference > 0 and  difference == 3:
         prize_id = 3

    elif difference > 0 and  difference == 4:
         prize_id = 4

    elif difference > 0 and  difference == 5:
         prize_id = 5

    elif difference > 0 and  difference == 6:
         prize_id = 6
        
    else:
         prize_id = 7
    
    user_number = request.POST.get("user_number")
    
    context = {
        'prize_id':   prize_id,
        'user_number':user_number
    }
    if User.objects.filter(number=user_number):
        return render(request, 'turntable/number_used.html',context)
    else:
       new_user = User(number=user_number)
       new_user.save()
       return render(request, 'turntable/turntable.html',context)
       


def prizes(request):
    user_number = request.POST.get("user_number")
    prize_id = request.POST.get("prize_id")
    context = {
        'prize_id':   prize_id,
        'user_number':user_number
    }
    return render(request, 'turntable/prize.html',context)

def no_prizes(request):
    return render(request,'turntable/no_prize.html'
    )






