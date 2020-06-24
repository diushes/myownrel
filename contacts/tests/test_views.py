from rest_framework.test import APITestCase, RequestsClient
from rest_framework import status


class ContactAPITestCase(APITestCase):

    def test_answer_get(self):
        print("Test contact get")
        client = RequestsClient()
        url = 'http://127.0.0.1:8000/api/contact/'
        response = client.get(url=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)