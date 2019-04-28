from teacher.models import *
from django.db.models  import Count
from .tools  import *
import os


def survey(request) :
    result = {}
    if "survey" in request.POST :
        result["sclass"] = SurveyClass(request.POST["survey"])

    if "survey_select" in request.POST :
        sel = request.POST["survey_select"]
        if sel == "new" :
            result['sclass'] = SurveyClass(0)
        else:
            result["sclass"] = SurveyClass(sel)
    
    if "create_survey" in request.POST :
        sf = SurveyForm(request.POST)
        if sf.is_valid() :
            sf.save()
    result["question_label_count"] = Question.objects.values("label").annotate(num_labels = Count("id"))
    result["survey_list"] = Survey.objects.all()
    return render(request,'manager/survey.html',context=result)
#------------------