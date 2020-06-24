from django.test import TestCase

from test_panel.models import Test, Question, Variant


class TestTestCase(TestCase):

    def setUp(self):
        print('Test setup activity')
        self.test = Test.objects.create(title='Religion')

    def test_test_into(self):
        self.assertEqual(self.test.title, 'Religion')


class QuestionTestCase(TestCase):

    def setUp(self):
        print('Question setup activity')
        self.test = Test.objects.create(title='Religion')
        self.question = Question.objects.create(test=self.test, question="Where is my socks?", answer="under the bed")

    def test_question_into(self):
        self.assertEqual(self.question.answer, "under the bed")


class VariantTest(TestCase):

    def setUp(self):
        print('Variant setup activity')
        self.test = Test.objects.create(title='Religion')
        self.question = Question.objects.create(test=self.test, question="Where is my socks?", answer="under the bed")
        self.variant = Variant.objects.create(question=self.question, version="under the bed")

    def test_variant_into(self):
        self.assertEqual(self.variant.version, "under the bed")