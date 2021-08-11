from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import *


# Create your views here.


def index(request):
    # get all the question in the server site
    latest_question_list = Questions.objects.order_by("-publication_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "votes/index.html", context)


# Chow specific question choices


def choice(request, question_id):
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "votes/choices.html", {"question": question})


# get the results of the votes


def results(request, question_id):
    # check out he database if not in the data base trought a error
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, "votes/results.html", {"question": question})


# Vote for a question choice

def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choices_set.get(pk=request.POST['choice'])
    except (KeyError, Choices.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'votes/results.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('voteLive:results', args=(question.id,)))
