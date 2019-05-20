from rest_framework import status,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.http import Http404


from django.contrib.auth.models import User
from django.db.models import Q
from .serializers import *

#=============================
class UserList(APIView):
  def get(self, request,  format=None) :
    user =  User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)
#=============================
class SurveyList(APIView):
  def get(self, request, format=None) :
    survey = Survey.objects.all()
    serializer = SurveySerializer(survey, many=True)      
    return Response(serializer.data)
#=============================
class SurveySearch(APIView):
  def get(self, request, id, format=None) :
    survey = Survey.objects.get(id=id)
    serializer = SurveySerializer(survey)      
    return Response(serializer.data)
#=============================
class QuestionSearch(APIView):
  def get(self, request, id, format=None) :
    question = Question.objects.filter(survey__id=id)
    serializer = QuestionSerializer(question, many=True)      
    return Response(serializer.data)
#=============================
class AnswerGet(APIView):
  def get(self, request, id, format=None) :
    answer = Answer.objects.filter(student__id=id)
    serializer = AnswerSerializer(answer, many=True)      
    return Response(serializer.data)
#=============================
class AnswerSend(APIView):
  def post(self, request, format=None):
    serializer = AnswerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#=============================
class StudentSend(APIView):
  def post(self, request, format=None):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#=============================
class CourseSearch(APIView):
  def get(self, request, format=None):
    course = Course.objects.all()
    serializer = CourseSerializer(course, many=True)
    return Response(serializer.data)
#=============================
class CourseGet(APIView):
  def get(self, request, id, format=None):
    course = Course.objects.get(id=id)
    serializer = CourseSerializer(course)
    return Response(serializer.data)
