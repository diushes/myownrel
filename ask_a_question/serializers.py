from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('name', 'question')

    def create(self, validated_data):
        return Question.objects.create(**validated_data)


class FAQQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'answer')

    def create(self, validated_data):
        return Question.objects.create(**validated_data)


class AnswerQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'answer', 'published_date')

    def create(self, validated_data):
        return Question.objects.create(**validated_data)