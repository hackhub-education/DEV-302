from django.shortcuts import render

from mysite.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
from .models import Subscriber


def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to DEV-302'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mail(subject,
                  message, EMAIL_HOST_USER, [recepient], fail_silently=False)

        # write to DB:
        new_user = Subscriber(email=recepient, status=1)
        new_user.save()

        # send back to success page
        context = {'recepient': recepient}
        return render(request, 'subscribe/success.html', context)
    else:
        return render(request, 'subscribe/index.html', {'form': sub})
