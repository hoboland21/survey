from rest_framework import status,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.http import Http404


from django.contrib.auth.models import User
from django.db.models import Q
from .serializers import UserSerializer



class UserList(APIView):
  def get(self, request,  format=None) :
    user =  User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)