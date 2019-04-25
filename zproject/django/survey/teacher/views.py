from django.shortcuts import render

# Create your views here.


def welcome(request) :
    result = {}
    return render(request,'teacher/welcome.html',context=result)