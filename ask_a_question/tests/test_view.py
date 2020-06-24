from rest_framework.test import APITestCase, RequestsClient
from rest_framework import status


class QuestionAPITestCase(APITestCase):

    def test_question_post(self):
        print("Test question post")
        client = RequestsClient()
        url = 'http://127.0.0.1:8000/api/question/'
        data = {"name": "John", "question": "Where is my socks?"}
        response = client.post(url=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AnswerAPITestCase(APITestCase):

    def test_answer_get(self):
        print("Test answer get")
        client = RequestsClient()
        url = 'http://127.0.0.1:8000/api/answer/'
        response = client.get(url=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FAQAPITestCase(APITestCase):

   def test_faq_get(self):
        print("Test FAQ get")
        client = RequestsClient()
        url = 'http://127.0.0.1:8000/api/faq/'
        response = client.get(url=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)