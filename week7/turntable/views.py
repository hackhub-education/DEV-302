from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from .models import Prizes, Player
from django.urls import reverse


def index(request):
    prize_list = Prizes.objects.order_by('-amount')
    context = {
        'prize_list':   prize_list
    }
    return render(request, 'turntable/index.html', context)


def phone_check(request):

    if request.method == 'POST':
        phone = request.POST.get("phone", "")

    player = Player.objects.filter(phone=phone)
    if player:
        return render(request, 'turntable/thank_you_1.html', {})
    else:
        # not found
        prize = Prizes(name="Pen", amount="2")
        prize.save()
        player = Player(phone=phone, prize=prize)
        player.save()
        return render(request, 'turntable/turntable.html', {'phone': phone, 'prize'=prize})

    # do a db check:

    # try:
    #     player_phone = player.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def thank_you_1(request):

    return render(request, 'turntable/thank_you_1.html', {})


def turntable(request):

    return render(request, 'turntable/turntable.html', {})
