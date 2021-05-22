from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('questions', views.show_questions, name = "questions"),
    path('question/<int:question_id>', views.show_question, name = 'question'),
    path('create_question/', views.create_question, name = "create_question"),
    path('create_question_view/', views.CreateQuestionView.as_view(), name = 'create_question_view'),
]