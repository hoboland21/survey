from teacher.models import *
from teacher.forms import *

from django.db.models  import Count
from .tools  import *



def layout(request) :
    result = {}
    survey = 0
    result["layout_form"] = LayoutForm()
    if "survey_id" in request.GET :
        survey = Survey.objects.get(id=request.GET["survey_id"])
        result['survey_form'] = SurveyForm(instance=survey)
        result["survey_id"] = request.GET["survey_id"]
    
    if "survey_id" in request.POST :
        survey = Survey.objects.get(id=request.POST["survey_id"])
        result['survey_form'] = SurveyForm(instance=survey)
        result["survey_id"] = request.POST["survey_id"]

    if "add_layout" in request.POST :
        ll = Layout()
        layout = LayoutForm(request.POST,instance=ll)
        if layout.is_valid():
            ll.survey = survey
            ll.save()
    if "edit_layout" in request.POST :
        layout = Layout.objects.get(id=request.POST["edit_layout"])
        result['layout_form'] = LayoutForm(instance=layout)
        result["layout"] = layout
        result["questions"] = Question.objects.all().order_by("label")
        result["items"] = Items.objects.filter(layout__id=layout.id)
    if "add_selected" in request.POST  and "q_select" in request.POST :
        seq = 10
        for q in request.POST.getlist("q_select") :
            i = Items()
            i.layout = layout
            i.question = Question.objects.get(id=q)
            i.sequence = seq 
            seq +=  5
            i.save()
    if survey :
        result["layouts"] = Layout.objects.filter(survey__id=survey.id)
    return render(request,'manager/layout.html',context=result)