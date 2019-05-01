from teacher.models import *
from teacher.forms import *
from django.db.models  import Count
from .upload import *
from .tools  import *
import os


#=============================
def add_question(sclass,quest) :
    item = Items()
    item.question = quest
    item.sequence = 1
    item.survey =sclass.survey
    item.page = 1
    item.save()                               
#=============================
def add_qlabel_list(request,sclass):
    for ql in request.POST.getlist("qlabel_list") :
        for quest in Question.objects.filter(label=ql) :
            if not Items.objects.filter(survey__id=sclass.survey.id,question__id=quest.id) :
                add_question(sclass,quest)
#=============================
def survey(request) :
    result = {}
    sclass = 0
    if "update_item" in request.POST :
        item = Items.objects.get(id=request.POST["update_item"])
        item.page = request.POST["page"]
        item.sequence = request.POST["sequence"]
        item.save()

    if "label_select" in request.POST :
        label_questions = Question.objects.filter(label=request.POST["label_select"])
        if request.POST["last_label_select"] == ""  :
            result["last_label_select"] = request.POST["label_select"]
        elif request.POST["last_label_select"]  == request.POST["label_select"]: 
            label_questions = []
        result["label_questions"] = label_questions 
        result["label_select"] = request.POST["label_select"]
    
    if "item_delete" in request.POST :
        Items.objects.get(id=request.POST["item_delete"]).delete()
 
    if "survey" in request.POST :
        sclass = SurveyClass(request.POST["survey"])
        result["survey"] = request.POST['survey']
        if "add_selected" in request.POST :
            if "qlabel_list" in request.POST :
                add_qlabel_list(request,sclass)

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
        upload_file(request)
    
    result["qlabels"] = qlabel_maker()
    result["question_upload_form"] = ImportFileForm()
    result["survey_list"] = Survey.objects.all()

    return render(request,'manager/survey.html',context=result)
#=============================
def qlabel_maker() :
    ql= Question.objects.values("label").annotate(num_labels = Count("id"))
    qlabels = []
    for q in ql :
        qq = Question.objects.filter(label=q["label"])
        qlabels.append({"label":q["label"], "number":q["num_labels"], "questions":qq})
    return qlabels