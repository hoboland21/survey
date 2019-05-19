from django.contrib.auth.models import User
from teacher.models  import *

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model= User
    fields = ('username', 'email', 'is_staff')

class SurveySerializer(serializers.ModelSerializer):
  class Meta:
    model= Survey
    fields = '__all__'
    
class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model= Question
    fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model= Student
    fields = '__all__'
    
class AnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model= Answer
    fields = '__all__'
    
class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model= Course
    fields = '__all__'
