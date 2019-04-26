from teacher.models import *
from django.db.models  import Count
from .tools  import *
import os

QFIELDS = ["question_type", "question", "label", "group"]

def delfile(id) :
    dobj = ImportFile.objects.get(id=id)
    os.remove(dobj.document.path)
    dobj.delete()

def import_file(id) :
    dobj = ImportFile.objects.get(id=id)
    file_obj = csv_read(dobj.document.path)
    
    for rec in file_obj :
        question = Question()
        for qf in QFIELDS :
            setattr(question,qf,rec[qf])
        question.save()

def screate(request) :
    result = {}
    if "create_survey" in request.POST :
        sf = SurveyForm(request.POST)
        if sf.is_valid() :
            sf.save()
   
    result["survey_list"] = Survey.objects.all()
    result["file_list"] = ImportFile.objects.all()
    result["question_label_count"] = Question.objects.values("label").annotate(num_labels = Count("id"))
    result["questions"] = Question.objects.all()
    result["survey"] = SurveyForm()

    if "action" in request.POST :
        action = request.POST["action"]
        for f in request.POST.getlist('file_select') :
            if action == "delete" :
                delfile(f)
            elif action == "upload" :
                import_file(f)

    result["questions"] = Question.objects.all()
    
    return render(request,'manager/screate.html',context=result)
#------------------