"""survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path, include
from django.views.decorators.csrf import ensure_csrf_cookie
from teacher.views import welcome
from manager.survey import survey

from django.views.generic import TemplateView


urlpatterns = [
    path('',admin.site.urls),
    path('admin/', admin.site.urls),
    path('_survey/',survey,name="survey"),
    path('webapi/',include ('webapi.urls')),
    re_path(r'^main/.*$', ensure_csrf_cookie(TemplateView.as_view(template_name="ang/main.html")),name="main"),
   ]   

