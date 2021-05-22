from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View

from .models import Question, Choice
from .forms import QuestionForm, ChoicesForm

from datetime import datetime as dt


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def show_question(request, question_id):

	question = Question.objects.get(id=question_id)
	choices = Choice.objects.all().filter(question = question)
	return render(
		request,
		"polls/question.html",
		{
			"question":question,
			"choices":choices
		}

		)

def show_questions(request):
	questions = Question.objects.all()
	return render(
		request,
		"polls/questions.html",
		{
			"questions":questions,
		}
		)

def create_question(request):

	if request.method == "POST":

		form = QuestionForm(request.POST)
		if form.is_valid():
			new_question = form.save(commit = False)
			new_question.pub_date = dt.now()
			new_question.save()

			return redirect("question", question_id = new_question.id)
		return redirect("create_question")
	else:

		form = QuestionForm()

		return render(
				request,
				"polls/create_question.html",
				{
					"form":form,
					"class": False,
				}
			)

class CreateQuestionView(View):

	def get(self, request, *args, **kwargs):

		question_form = QuestionForm()
		choices_form = ChoicesForm()

		return render(
				request,
				'polls/create_question.html',
				{
					"question_form": question_form,
					"choices_form": choices_form,
					"class": True
				})

	def post(self, request, *args, **kwargs):

		question_form = QuestionForm(request.POST)
		choices_form = ChoicesForm(request.POST)

		if question_form.is_valid() and choices_form.is_valid():
			new_question = question_form.save(commit = False)
			new_question.pub_date = dt.now()
			new_question.save()

			choices = choices_form.cleaned_data['choice_text'].split(',')
			for choice in choices:
				Choice.objects.create(question = new_question, choice_text = choice.strip())

			return redirect("question", question_id = new_question.id)

		return redirect("create_question_view")



	


	

