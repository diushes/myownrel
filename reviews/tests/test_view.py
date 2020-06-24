from django.test import TestCase, Client
from rest_framework import status

from reviews.models import *
from reviews.serializers import *
from django.urls import reverse


client = Client()
class CreateProductTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_details(self):
        post_data = {
            'name':'Stefan',
            'review_text':'Amazing app'
        }
        response = self.client.post(reverse('reviews:reviews'), post_data)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)