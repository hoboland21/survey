from django.shortcuts import render



def screate(request) :
    result = {}
    return render(request,'manager/screate.html',context=result)