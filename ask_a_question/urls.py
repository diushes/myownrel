from django.urls import path, include
from . import views


urlpatterns = [
    path('question/', views.QuestionView.as_view()),
    path('answer/', views.AnswerView.as_view()),
    path('faq/', views.FAQView.as_view()),
]