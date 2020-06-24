from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Test
from .serializers import TestSerializer, TestDetailSerializer


class TestListAPIView(APIView):

    def get(self, request):
        tests = Test.objects.exclude(questions__isnull=True)
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)


class TestDetailAPIlView(APIView):

    def get(self, request, pk):
        test = Test.objects.get(pk=pk)
        serializer = TestDetailSerializer(test)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        test = Test.objects.get(pk=pk)
        serializer = TestDetailSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)