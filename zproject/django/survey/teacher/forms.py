from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, Form, Textarea, TextInput, HiddenInput,PasswordInput,DateInput
from teacher.models import  * 
from datetime import datetime 

#================================
class SurveyForm(ModelForm) :
    class Meta:
        model = Survey
        exclude = ["id","locked",]

#================================
class QuestionForm(ModelForm) :
    class Meta:
        model = Question
        exclude = ["id",]

#================================
class ImportFileForm(forms.ModelForm):
    class Meta:
        model = ImportFile
        fields = ('document', )
