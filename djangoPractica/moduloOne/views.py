from django.shortcuts import render, HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "moduloOne/index.html", context)

def detail(request, question_id):
        try:
               question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
               raise Http404("Question does not exist")
        return render(request, "moduloOne/detail.html", {"question": question})

def results(request, question_id):
        response = "You are looking at the results of the question %s."
        return HttpResponse(response % question_id)

def vote(request, question_id):
        return HttpResponse("You are voting on question %s." % question_id)

