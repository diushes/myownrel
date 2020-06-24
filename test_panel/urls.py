from django.urls import path

from .views import TestListAPIView, TestDetailAPIlView

urlpatterns = [
    path('test/', TestListAPIView.as_view()),
    path('test/<int:pk>', TestDetailAPIlView.as_view()),
]