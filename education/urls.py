from .views import *
from django.urls import path

app_name = 'education'
urlpatterns = [
    path('religions/', ReligionsListView.as_view(), name='religions'),
    path('topics/', TopicsListView.as_view(), name='topics'),
    path('subtopics/', SubTopicsListView.as_view(), name='subtopics'),
    path('topicsByReligion/<int:pk>/', TopicsByReligionView.as_view(), name='topicsByReligion'),
    path('subtopicsByTopic/<int:pk>/', SubtopicByTopic.as_view(), name='subtopicByTopic')
    ]