from django.test import TestCase
from reviews.serializers import *
from reviews.models import *

class ReligionSerializerTest(TestCase):
    def setUp(self) -> None:
        serializer_data = {'name':'Damon', 'review_text':'Very uuseful app'}

        self.review = Review.objects.create(**serializer_data)
        self.serializer = ReviewSerializer(instance=self.review)


    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'name', 'review_text'])





