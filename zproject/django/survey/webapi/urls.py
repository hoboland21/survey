"""mcsap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from .views import StudentIdNew, StudentsSearch,UserSearch,StudentId,TagSearch
from .views import ParentTagNew, ParentTagView, StudentRegisterView,RegisterView 
from .views import RegisterNewView, StudentParentTagSearch, Parent, ParentNew
from .views import ParentUserView, AgreementView, AgreementViewNew, AgreementViewReg
from .views import ContractView
from .mailapi import MailPost,SystemConfigView

urlpatterns = [
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    # mail service
    path('mail/', MailPost.as_view()),
    #Student Service GetPrimaryStudents
    path('students/<int:pid>/',StudentsSearch.as_view()),
    #Register Service viewing Students records
    path('student/register/<int:pk>/',StudentRegisterView.as_view()),
    # Register create
    path('register/',RegisterNewView.as_view()),
    # Register view, delete, put
    path('register/<int:pk>/',RegisterView.as_view()),
   #Parent Service
    path('user/<int:pid>/',UserSearch.as_view()), 
    
    # Student Service Get, Put, Delete  Student
    path('studentid/<int:pk>/',StudentId.as_view()),
    # Student Service Post

    path('studentid/',StudentIdNew.as_view()),

    # Parent Tag Service
    path('tag/<parent_card>/<student_card>/',TagSearch.as_view()),

    # Student Parent Tag search
    path('studtags/<sid>/',StudentParentTagSearch.as_view()),

    # Parent Tag Service
    path('parenttag/',ParentTagNew.as_view()),
    # Parent Tag Service
    path('parenttag/<int:pk>/',ParentTagView.as_view()),

 
    #System Default information Improved
    path('system/sysconfig/',SystemConfigView.as_view()),
   
   # Student Service Get, Put, Delete  Parent
    path('parent/<int:pk>/',Parent.as_view()),
    # Student Service Post

    path('parent/',ParentNew.as_view()),

    # Parent user
    path('parentuser/<username>/',ParentUserView.as_view()),

    # Agreements
    path('agreement/<int:pk>/',AgreementView.as_view()),

    path('agreement/',AgreementViewNew.as_view()),

    path('agreement/reg/<int:register>/',AgreementViewReg.as_view()),

    path('contract/<name>/',ContractView.as_view()),
]   

urlpatterns=format_suffix_patterns(urlpatterns)

