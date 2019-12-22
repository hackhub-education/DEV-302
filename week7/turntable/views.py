from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from .models import Prizes
from django.urls import reverse


def index(request):
    prize_list = Prizes.objects.order_by('-amount')
    context = {
        'prize_list':   prize_list

    }
    return render(request, 'turntable/index.html', context)
