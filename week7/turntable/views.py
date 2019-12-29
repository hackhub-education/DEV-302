from django.shortcuts import render, get_object_or_404


from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from django.urls import reverse

from .models import Prizes,User


def index(request):
    prize_list = Prizes.objects.order_by('-amount')
    context = {
        'prize_list':   prize_list

    }
    return render(request, 'turntable/index.html', context)



def phoneno(request):
    user_number = request.POST.get("user_number")
    if  User.object.filter(number=user_number).exist():
        prize = randint(0, 10)
        prize_id = prize
        context = {
        'price_id':   prize_id,
        'price':   prize,
        }
       return render(request, 'turntable/number_used.html', context)
    else:
       new_user = User(number=user_number)
       new_user.save()
       return render(request, 'turntable/turntable.html')


