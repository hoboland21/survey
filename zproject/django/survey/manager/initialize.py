from teacher.models import *
from teacher.forms import *
from django.db.models  import Count
from .upload import *
from .tools  import *
import os


def initialize(request) :
  result = {}
  result["course_upload_form"] = ImportFileForm()

  if "upload_course" in request.POST :
     upload_course(request)

  return render(request,"manager/initialize.html",context=result)