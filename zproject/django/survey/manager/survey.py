from teacher.models import *
from teacher.forms import *
from django.db.models  import Count
from .tools  import *
import os


def survey(request) :
    result = {}
    if "new_layout" in request.POST: 
        result["layout_form"] = LayoutForm()
            
    
    if "survey" in request.POST :
        sclass = SurveyClass(request.POST["survey"])
        if "layout" in request.POST :
            sclass.set_layout(request.POST["layout"])
        
        if "add_layout" in request.POST :
            layout = Layout()
            layout_form = LayoutForm(request.POST, instance=layout)
            if layout_form.is_valid() :
                layout.survey = sclass.survey
                layout.save()
                sclass.set_layout(layout.id)

        if "layout_select" in request.POST:
            sel = request.POST["layout_select"]
            if sel == "new" :
                sclass.set_layout(0)
            elif sel == "null" :
                pass    
            else:
                sclass.set_layout(sel)
        result["sclass"] = sclass

    if "survey_select" in request.POST :
        sel = request.POST["survey_select"]
        if sel == "new" :
            result['sclass'] = SurveyClass(0)
        elif sel == "null" :
            pass    
        else:
            result["sclass"] = SurveyClass(sel)
    
    if "create_survey" in request.POST :
        sf = SurveyForm(request.POST)
        if sf.is_valid() :
            sf.save()
    if "select_questions" in request.POST :
        result["select_questions"] = True

    ql= Question.objects.values("label").annotate(num_labels = Count("id"))
    qlabels = []
    for q in ql :
        qq = Question.objects.filter(label=q["label"])
        qlabels.append({"label":q["label"], "number":q["num_labels"], "questions":qq})
    
    result["qlabels"] = qlabels
    
    if "show_questions" in request.POST :
        result["show_questions"] = request.POST["show_questions"]

    result["survey_list"] = Survey.objects.all()
    return render(request,'manager/survey.html',context=result)
#------------------