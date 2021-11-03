from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import *

def index(request):
    context={
        'questions': Question.objects.all(),
    }
    return render(request, 'polls/index.html', context)

def detail(request, pk):
#    return HttpResponse(f'Detail Question id={pk}')
    context = {
        'question': Question.objects.get(pk=pk),
    }
    return render(request, 'polls/detail.html', context)

def results(request, pk):
#    return HttpResponse(f'Results Question id={pk}')
    context = {
        'question': Question.objects.get(pk=pk),
    }
    return render(request, 'polls/results.html', context)

def vote(request, pk):
 #   return HttpResponse(f'Vote Question id={pk}')
    question= Question.objects.get(pk=pk)
    try:
        choice_id=int(request.POST.get('choice'))
        selected_choice=question.choice_set.get(pk=choice_id)
    except:
        context={
            'question': question,
            'error_message': 'Be careful!'
        }
        return render(request,'polls/detail.html', context)
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(pk,)))
# Create your views here.
