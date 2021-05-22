from django.forms import ModelForm
from django import forms

from .models import Question


class QuestionForm(ModelForm):

	class Meta:
		model = Question
		fields = ['question_text']
		labels = {"question_text": "Question "}

class ChoicesForm(forms.Form):

	choice_text = forms.CharField(label = 'Choices', max_length = 200)