from rest_framework import serializers
from .models import *


class QuestionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Question
        fields = ('ques', 
                  'a', 
                  'b', 
                  'c', 
                  'd'
                )
        
class Answerserializer(serializers.ModelSerializer):
    class Meta():
      model = Answer
      fields = '__all__'