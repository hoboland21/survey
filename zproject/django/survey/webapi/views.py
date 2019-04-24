from rest_framework import status,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.http import Http404


from .serializers import StudentCardSerializer, ParentCardSerializer, ParentTagSerializer, RegisterSerializer, UserSerializer
from .serializers import ContractSerializer, AgreementSerializer
from portal.models import StudentCard, ParentCard, ParentTag

from portal.models import Register, Agreement, Contract
from django.contrib.auth.models import User
from django.db.models import Q


class StudentsSearch(APIView):
  def get(self, request, pid, format=None) :
    students = StudentCard.objects.filter(parenttag__parent_card = pid,parenttag__parents_web="Yes")
    serializer = StudentCardSerializer(students, many=True)
    return Response(serializer.data)

#-----------------------------------------------------
class UserSearch(APIView):
  def get(self, request, pid, format=None) :
    parent = ParentCard.objects.get(id=pid)
    serializer = ParentCardSerializer(parent)
    return Response(serializer.data)
#-----------------------------------------------------
class TagSearch(APIView):
  def get(self, request, parent_card, student_card, format=None) :
    tag = ParentTag.objects.get(parent_card = parent_card, student_card=student_card)
    serializer = ParentTagSerializer(tag)
    return Response(serializer.data)
#-----------------------------------------------------
class StudentIdNew(APIView):
  def post(self, request, format=None):
    serializer = StudentCardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-----------------------------------------------------
class StudentId(APIView) :
  def get_object(self,pk):
    try:
      return StudentCard.objects.get(pk=pk)
    except StudentCard.DoesNotExist:
      raise Http404
  
  def get (self, request, pk, format=None) :
    student = self.get_object(pk)
    serializer = StudentCardSerializer(student)
    return Response(serializer.data)

  def put (self, request, pk, format=None):
    student = self.get_object(pk)
    serializer = StudentCardSerializer(student, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete ( self, request, pk, format=None):
    student = self.get_object(pk)
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#-----------------------------------------------------
class ParentTagNew(APIView):
  def post(self, request, format=None):
    serializer = ParentTagSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-----------------------------------------------------
class StudentParentTagSearch(APIView):
  def get(self, request, sid, format=None) :
    tags = ParentTag.objects.filter(student_card=sid).order_by('family_order')
    serializer = ParentTagSerializer(tags, many=True)
    return Response(serializer.data)

#-----------------------------------------------------
class ParentTagView(APIView) :
  def get_object(self,pk):
    try:
      return ParentTag.objects.get(pk=pk)
    except ParentTag.DoesNotExist:
      raise Http404

  def get (self, request, pk, format=None) :
    tag = self.get_object(pk)
    serializer = ParentTagSerializer(tag)
    return Response(serializer.data)



  def put (self, request, pk, format=None):
    tag = self.get_object(pk)
    serializer = ParentTagSerializer(tag, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete ( self, request, pk, format=None):
    tag = self.get_object(pk)
    tag.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



#-----------------------------------------------------
class StudentRegisterView(APIView) :
  def get_object(self,pk):
    try:
      return Register.objects.filter(student_card=pk).order_by("-schoolyear")
    except Register.DoesNotExist:
      raise Http404
  
#-----------------------------------------------------

  def get (self, request, pk, format=None) :
    register = self.get_object(pk)
    serializer = RegisterSerializer(register, many=True)
    return Response(serializer.data)

#-----------------------------------------------------

class RegisterView(APIView) :
  def get_object(self,pk):
    try:
      return Register.objects.get(pk=pk)
    except Register.DoesNotExist:
      raise Http404
  
  def get (self, request, pk, format=None) :
    reg = self.get_object(pk)
    serializer = RegisterSerializer(reg)
    return Response(serializer.data)

  def put (self, request, pk, format=None):
    reg = self.get_object(pk)
    serializer = RegisterSerializer(reg, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete ( self, request, pk, format=None):
    reg = self.get_object(pk)
    reg.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#-----------------------------------------------------
class RegisterNewView(APIView):
  def post(self, request, format=None):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#-----------------------------------------------------

#-----------------------------------------------------

class ParentNew(APIView):
  def post(self, request, format=None):
    serializer = ParentCardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-----------------------------------------------------
class Parent(APIView) :
  def get_object(self,pk):
    try:
      return ParentCard.objects.get(pk=pk)
    except ParentCard.DoesNotExist:
      raise Http404
 #------------ 
  def get (self, request, pk, format=None) :
    parent = self.get_object(pk)
    serializer = ParentCardSerializer(parent)
    return Response(serializer.data)
 #------------ 

  def put (self, request, pk, format=None):
    parent = self.get_object(pk)
    serializer = ParentCardSerializer(parent, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 #------------ 

  def delete ( self, request, pk, format=None):
    parent = self.get_object(pk)
    parent.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
#-----------------------------------------------------
class ParentUserView(APIView):
  def get_object(self,username):
    try:
      return ParentCard.objects.get(username=username)
    except ParentCard.DoesNotExist:
      raise Http404
  def get(self, request, username, format=None) :
    parent = self.get_object(username)
    serializer = ParentCardSerializer(parent)
    return Response(serializer.data)
#-----------------------------------------------------

class AgreementView(APIView) :
  def get_object(self,pk):
    try:
      return Agreement.objects.get(pk=pk)
    except Agreement.DoesNotExist:
      raise Http404
 #------------ 
  def get (self, request, pk, format=None) :
    agree = self.get_object(pk)
    serializer = AgreementSerializer(agree)
    return Response(serializer.data)
 #------------ 

  def put (self, request, pk, format=None):
    agree = self.get_object(pk)
    serializer = AgreementSerializer(agree, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 #------------ 

  def delete ( self, request, pk, format=None):
    agree = self.get_object(pk)
    agree.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
#-----------------------------------------------------
class AgreementViewNew(APIView) :
  def post(self, request, format=None):
    serializer = AgreementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#-----------------------------------------------------
class AgreementViewReg(APIView) :
  def get_object(self,register):
    try:
      return Agreement.objects.filter(register=register)
    except Agreement.DoesNotExist:
      raise Http404
  
  def get(self, request, register, format=None) :
    agree = self.get_object(register)
    serializer = AgreementSerializer(agree, many=True)
    return Response(serializer.data)
#-----------------------------------------------------

class ContractView(APIView) :
  def get_object(self,name):
    try:
      return Contract.objects.get(name=name)
    except Contract.DoesNotExist:
      raise Http404
 #------------ 
  def get (self, request, name, format=None) :
    contract = self.get_object(name)
    serializer = ContractSerializer(contract)
    return Response(serializer.data)
 #------------ 
