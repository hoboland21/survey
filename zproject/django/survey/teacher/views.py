from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.


def welcome(request) :
    result = {}
    result["surveys"] = Survey.objects.all()
    return render(request,'teacher/welcome.html',context=result)


def testing(request,id) :
    print(request.POST)
    result = {}
    result["survey"] = Survey.objects.get(id=id)
    result["questions"] = Question.objects.filter(survey__id=id)
    result["current"] = 0
    return render(request,'teacher/testing.html',context=result)