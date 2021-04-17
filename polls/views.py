from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def show_question(request, question_id):

	question = Question.objects.get(id=question_id).question_text
	return HttpResponse(f"Hello, your question is {question}")

def show_questions(request):
	questions = Question.objects.all()
	return render(
		request,
		"polls/questions.html",
		{
			"questions":questions,
		}
		)