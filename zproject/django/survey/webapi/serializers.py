from django.contrib.auth.models import User

from rest_framework import serializers
from portal.models import StudentCard, ParentCard, ParentTag, Register
from portal.models import Message, Agreement, Contract


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model= User
    fields = ('username', 'email', 'is_staff')

class StudentCardSerializer(serializers.ModelSerializer):
  class Meta:
    model= StudentCard
    fields = '__all__'
    
class ParentCardSerializer(serializers.ModelSerializer):
  class Meta:
    model= ParentCard
    fields = '__all__'
class ParentTagSerializer(serializers.ModelSerializer):
  class Meta:
    model= ParentTag
    fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model= Register
    fields = '__all__'       


class AgreementSerializer(serializers.ModelSerializer) :
  class Meta:
    model= Agreement
    fields = '__all__'

class ContractSerializer(serializers.ModelSerializer) :
  class Meta:
    model= Contract
    fields = '__all__'
