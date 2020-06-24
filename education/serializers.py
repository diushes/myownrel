from rest_framework import serializers
from .models import *

class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'



class SubtopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subtopic
        fields = '__all__'




