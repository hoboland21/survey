from teacher.forms import ImportFileForm, SurveyForm
from teacher.models import ImportFile , Survey, Question, Course
from .tools import *
import os

#------------------
QFIELDS = ["format","question","sequence"]
COURSE_FIELDS = ["department","title","name","section","instructor"]
#------------------
def delfile(id) :
    dobj = ImportFile.objects.get(id=id)
    os.remove(dobj.document.path)
    dobj.delete()
#------------------
def add_questions(doc,survey) :
    qlist = csv_read(doc.document.path) 
    old_questions = Question.objects.filter(survey__id=survey.id)
    for oq in old_questions :
        oq.delete()

    for q in qlist :
        question =Question()
        question.survey = survey
        for qf in QFIELDS :
            setattr(question,qf,q[qf])
        question.save()
#------------------
def upload_file(request,sclass) :
    import_file = ImportFile()
    form = ImportFileForm(request.POST, request.FILES, instance=import_file)
    if form.is_valid():
        import_file.save()  
        add_questions(import_file,sclass.survey)
        delfile(import_file.id)
#------------------
def add_course(doc) :
    clist = csv_read(doc.document.path) 
    for c in clist :
        course =Course()
        for cf in COURSE_FIELDS :
            setattr(course,cf,c[cf])
        course.save()
#------------------
def upload_course(request) :
    import_file = ImportFile()
    form = ImportFileForm(request.POST, request.FILES, instance=import_file)
    if form.is_valid():
        import_file.save()  
        add_course(import_file)
        delfile(import_file.id)
