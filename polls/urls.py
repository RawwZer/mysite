from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('questions', views.show_questions, name = "questions"),
    path('question/<int:question_id>', views.show_question, name = 'question')
]