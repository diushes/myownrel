from rest_framework import serializers

from .models import Test, Question, Variant


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ('id', 'question', 'version')


class QuestionSerializer(serializers.ModelSerializer):

    variants = VariantSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'test', 'question', 'answer', 'variants')


class TestSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = ('id', 'title', 'level', 'questions',
                  'questions_count', 'passed_the_test')


class TestDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ('id', 'passed_the_test')