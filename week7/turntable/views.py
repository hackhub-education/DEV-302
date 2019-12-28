from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from . import forms
from .models import Prizes,User
from django.urls import reverse


def index(request):
    prize_list = Prizes.objects.order_by('-amount')
    context = {
        'prize_list':   prize_list

    }
    return render(request, 'turntable/index.html', context)

def start(request):
    sub = forms.start()
    if request.method=='POST':
        sub = forms.start(request.POST)
        user_phone = str(sub['user_phone'].value())

        print("\n\nFROM PHONE: ", user_phone)
        if not User.objects.filter(user_phone=user_phone).exists():
            context = {'user_phone':user_phone}
            return render(request, 'turntable/turntable_page.html',context)
        else:
            context = {'user_phone':user_phone}
            return render(request, 'turntable/invalid_user_page.html',context)
    return render(request, 'turntable/get_phone.html', {'form':sub})
    