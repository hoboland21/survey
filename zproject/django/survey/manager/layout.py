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
    if survey :
        result["layouts"] = Layout.objects.filter(survey__id=survey.id)
    return render(request,'manager/layout.html',context=result)