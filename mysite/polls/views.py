from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "Você esta olhando os resultados da questao %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Voce esta votando na questao %s." % question_id)


