from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from .models import Prizes,Users
from django.urls import reverse
from .froms import Subscribe



def index(request):
    prize_list = Prizes.objects.order_by('-amount')
    
    context = {
        'prize_list':   prize_list

    }
 
    new_user = Users(Phone=PhoneNumber)
    new_user.save()
    return render(request, 'turntable/index.html', context)

def phoneno(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
       phone(subject,[poster], fail_silently=False)
       new_user = Subscriber(Phone=poster, status=1)
       new_user.save()
       context = {
            'poster': poster
                 }
       return render(request, 'turntable/index.html', context)
    else:
       return render(request, 'turntable/Thankyou2.html', {'form': sub})








