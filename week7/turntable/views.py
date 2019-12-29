from django.shortcuts import render, get_object_or_404
import random
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from . import forms
from .models import Prizes,User
from django.urls import reverse


def index(request):
    return render(request, 'turntable/index.html')

def start(request):
    user_phone = request.POST['user_phone']

    print("\n\nFROM PHONE: ", user_phone)
    if not User.objects.filter(user_phone=user_phone).exists():
        prizes_list = Prizes.objects.filter(amount!=0).order_by('-id')
        # create a random range and generate a dice for prize
        range = 100
        for prize in prizes_list:
            range += prize['amount']
        prize_dice = random.randint(0,range)
        dice_level = 100
        # define the prize base on the generated dice
        if prize <= dice_level:
            prize_id=7
        else:
            for prize in prizes_list:
                dice_level += prize['amount']
                prize_id = prize['id']
                if prize_dice < dice_level:
                    break
        
        context = {'user_phone':user_phone, 'prize_id':prize_id}
        return render(request, 'turntable/turntable.html', context)
    else:
        context = {'user_phone':user_phone}
        return render(request, 'turntable/number_used.html', context)

def reward(request):
    phone = request.POST['user_phone']
    prize = request.POST('prize_id')
    reward=Prizes.objects.filter(id=prize)
    user = User(user_phone=phone, prize_name=reward['name'])
    # user.save()
    return render(request, 'turntable/prize.html',)

    