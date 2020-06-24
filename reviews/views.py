from django.shortcuts import render
from .serializers import *
from rest_framework.generics import CreateAPIView
# Create your views here.

class Reviewview(CreateAPIView):
    model = Review
    serializer_class = ReviewSerializer
