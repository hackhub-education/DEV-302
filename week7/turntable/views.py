from django.shortcuts import render, get_object_or_404
import random
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader
from . import forms
from .models import Prizes,User
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'turntable/index.html')

def start(request):
    user_phone = request.POST['user_phone']

    if not User.objects.filter(user_phone=user_phone).exists():
        
        context = {'user_phone':user_phone}
        return render(request, 'turntable/turntable.html', context)
    else:
        context = {'user_phone':user_phone}
        return render(request, 'turntable/number_used.html', context)

def reward(request):
    result = request.POST
    if request.POST:
        phone = result.get('user_phone')
        prize = result.get('prize_id')

        reward=Prizes.objects.get(id=prize)
        current_user = User(user_phone=phone, prize_name=reward.name)
        if prize != '7':
            reward.amount -= 1
        reward.save()
        current_user.save()
        context = {'user_phone':phone, 'prize_id':reward.id, 'prize_name':reward.name, 'img':'turntable/img/'+str(reward.id)+'.png'}
        if prize == '7':
            return render(request, 'turntable/no_prize.html',context)
        else:
            return render(request, 'turntable/prize.html',context)

@csrf_exempt
def lottery_ajax(request):
    prizes_list = Prizes.objects.filter(amount__gt=0).order_by('-id')
    # create a random range and generate a dice for prize
    range = 10
    for prize in prizes_list:
        range += prize.amount
    prize_dice = random.randint(0,range)
    dice_level = 10
    prize_id = 7
    # define the prize base on the generated dice
    if prize_dice <= dice_level:
        prize_id=7
    else:
        for prize in prizes_list:
            dice_level += prize.id
            prize_id = prize.id
            if prize_dice < dice_level:
                break
    
    response = {'prize_id':prize_id}
    return JsonResponse(response)

    