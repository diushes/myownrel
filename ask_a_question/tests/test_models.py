from django.test import TestCase

from ask_a_question.models import Question


class QuestionTestCase(TestCase):
    # Question Test
    def setUp(self):
        print('Setup Question Activity')
        self.question = Question.objects.create(name="John",
                                                question="Where is my socks?")

    def test_question_into(self):
        self.assertEqual(self.question.name, 'John')