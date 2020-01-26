from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question, 'question_id':question_id})

@csrf_exempt
def vote_ajax(request):
    question_id = request.POST['question_id']
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return {
            "msg": "Vote unsuccess, please try again. (Reason: Choice.DoesNotExist)",
            'stauts': "unsuccess"
        }

    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        choice_list = []
        for choice in question.choice_set.all():
            choice_list.append({'text':choice.choice_text,'votes':choice.votes})
        response = {'msg':"success", 'data':choice_list}
        return JsonResponse(response)


def setcookie(request):
    html = HttpResponse("<h1>Django Cookie Tutorial</h1>")
    if request.COOKIES.get('visits'):
        html.set_cookie('mycookie', 'Welcome Back')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "Welcome for the first time"
        html.set_cookie('visits', value)
        html.set_cookie('mycookie', text)
    return html
 


def showcookie(request):
    show = request.COOKIES['mycookie']
    html = f"<center> New Page <br>{show}</center>"
    return HttpResponse(html)


def deletecookie(request):
    if request.COOKIES.get('visits'):
       response = HttpResponse("<h1>Cookie deleted</h1>")
       response.delete_cookie("visits")
    else:
        response = HttpResponse("<p>need to create cookie before deleting</p>")
    return response