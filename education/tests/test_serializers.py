from django.test import TestCase
from education.serializers import *
from education.models import *

class ReligionSerializerTest(TestCase):
    def setUp(self) -> None:
        serializer_data = {'name':'Ислам'}

        self.religion = Religion.objects.create(**serializer_data)
        self.serializer = ReligionSerializer(instance=self.religion)


    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'name'])


class TopicSerializerTest(TestCase):
    def setUp(self) -> None:
        religion = Religion.objects.create(name='Ислам')
        serializer_data = {'title': 'История возникновения', 'religion':religion}

        self.topic = Topic.objects.create(**serializer_data)
        self.serializer = TopicSerializer(instance=self.topic)
    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'title', 'religion'])


class SubTopicSerializerTest(TestCase):
    def setUp(self) -> None:
        religion = Religion.objects.create(name='Ислам')
        topic = Topic.objects.create(title='История возникновения', religion=religion)
        serializer_data = {'title':'Some title', 'content':'Some content', 'topic':topic}

        self.subtopic = Subtopic.objects.create(**serializer_data)
        self.serializer = SubtopicSerializer(instance=self.subtopic)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'title', 'content','topic'])



