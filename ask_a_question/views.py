from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Question
from .serializers import QuestionSerializer, FAQQuestionSerializer, AnswerQuestionSerializer


class QuestionView(APIView):

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerView(APIView):

    def get(self, request):
        answers = Question.objects.exclude(answer__isnull=True).exclude(answer__exact='').exclude(faq=True)
        serializer = AnswerQuestionSerializer(answers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FAQView(APIView):

    def get(self, request):
        answer = Question.objects.filter(faq=True)
        serializer = FAQQuestionSerializer(answer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)