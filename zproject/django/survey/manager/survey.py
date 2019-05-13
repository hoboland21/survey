from teacher.models import *
from teacher.forms import *
from django.db.models  import Count
from .upload import *
from .tools  import *
import os

#=============================
def survey(request) :
    result = {}
    sclass = 0

    if "update_item" in request.POST :
        q = Question.objects.get(id=request.POST["update_item"])
        q.sequence = request.POST["sequence"]
        q.save()
 
    if "survey" in request.POST :
        sclass = SurveyClass(request.POST["survey"])
        result["survey"] = request.POST['survey']

    if "survey_select" in request.POST :
        sel = request.POST["survey_select"]
        if sel == "new" :
            sclass = SurveyClass(0)
        elif sel == "null" :
            pass    
        else:
            sclass = SurveyClass(sel)
    
    if "create_survey" in request.POST :
        s = Survey()
        sf = SurveyForm(request.POST,instance=s) 
        if sf.is_valid() :
            s.save()
            sclass = SurveyClass(s.id)
    
    if sclass :
        result["sclass"] = sclass

    if "upload_file" in request.POST :
        if sclass.survey.locked == False :
            upload_file(request,sclass)

    result["question_upload_form"] = ImportFileForm()
    result["survey_list"] = Survey.objects.all()

    return render(request,'manager/survey.html',context=result)
