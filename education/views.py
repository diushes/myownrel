from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

class ReligionsListView(ListAPIView):
    model = Religion
    serializer_class = ReligionSerializer
    queryset = Religion.objects.all()

class TopicsListView(ListAPIView):
    model = Topic
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

class SubTopicsListView(ListAPIView):
    model = Subtopic
    serializer_class = SubtopicSerializer
    queryset = Subtopic.objects.all()

class TopicsByReligionView(ListAPIView):
    model = Topic
    serializer_class = TopicSerializer
    def get_queryset(self):
        return Topic.objects.filter(religion=self.kwargs['pk'])

class SubtopicByTopic(ListAPIView):
    model = Subtopic
    serializer_class = SubtopicSerializer
    def get_queryset(self):
        return Subtopic.objects.filter(topic=self.kwargs['pk'])

