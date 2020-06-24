from django.test import TestCase
from reviews.models import *

class ModelsTest(TestCase):
    def setUp(self) -> None:
        Review.objects.create(name='John', review_text='Good app')

    def test_review_name(self):
        review_name = Review.objects.get(id=1).name
        self.assertEquals(review_name, 'John')

    def test_review_text(self):
        review_text = Review.objects.get(id=1).review_text
        self.assertEquals(review_text, 'Good app')
