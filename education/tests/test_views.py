from django.test import TestCase, Client
from education.models import *
from education.serializers import *
from django.urls import reverse


client = Client()
class AllViewsTest(TestCase):
    def setUp(self) -> None:
        #creating some religions
        Religion.objects.create(name='Ислам')
        Religion.objects.create(name='Буддизм')
        Religion.objects.create(name='Христианство')
        #creating some topics
        for i in range(1,4):
            Topic.objects.create(title="История возникновения", religion_id=i)
            #creating some subtopics
            for j in range(4):
                Subtopic.objects.create(title='title #'+str(j), content='some content #'+str(j), topic_id=i)

    def test_get_all_religions_test(self):
        response = self.client.get(reverse('education:religions'))
        religions = Religion.objects.all()
        serializer = ReligionSerializer(religions, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_get_all_topics(self):
        response = self.client.get(reverse('education:topics'))
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_all_subtopics(self):
        response = self.client.get(reverse('education:subtopics'))
        subtopics = Subtopic.objects.all()
        serializer = SubtopicSerializer(subtopics, many=True)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_topics_by_religion(self):
        pk = 1
        response = self.client.get(reverse('education:topicsByReligion', kwargs={'pk':pk}))
        topicsOfReligion = Topic.objects.filter(religion_id=pk)
        serializer = TopicSerializer(topicsOfReligion, many=True)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_subtopics_by_topic(self):
        pk = 1
        response = self.client.get(reverse('education:subtopicByTopic', kwargs={'pk':pk}))
        subtopicsOfTopic = Subtopic.objects.filter(topic_id=pk)
        serializer = SubtopicSerializer(subtopicsOfTopic, many=True)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, 200)


