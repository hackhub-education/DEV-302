from django.http import HttpResponse, Http404, HttpResponseRedirect,JsonResponse
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render


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
    return render(request, 'polls/detail.html', {'question': question,'question_id': question_id})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})




def vote_ajax(request):
    question_id = request.POST['question_id']
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
         return HttpResponse("unsuccesful")

    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        all_choice = []
        for i in question.choice_set.all():
            all_choice.append({'text':i.choice_text,'vote':i.votes})
        
        response={
            "msg":"success",
            "data":all_choice}
        
  
        return JsonResponse(response)

