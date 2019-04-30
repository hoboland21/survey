from teacher.forms import ImportFileForm, SurveyForm
from teacher.models import ImportFile , Survey, Question, Items
from .tools import *
import os

#------------------
QFIELDS = ["format","question","label","group"]
#------------------
def delfile(id) :
    dobj = ImportFile.objects.get(id=id)
    os.remove(dobj.document.path)
    dobj.delete()

#------------------
def add_questions(doc) :
    qlist = csv_read(doc.document.path) 
    for q in qlist :
        if not Question.objects.filter(label=q["label"],question=q["question"],group=q["group"]) :
            question =Question()
            for qf in QFIELDS :
                setattr(question,qf,q[qf])
            question.save()

#------------------
def upload_file(request) :
    import_file = ImportFile()
    form = ImportFileForm(request.POST, request.FILES, instance=import_file)
    if form.is_valid():
        import_file.save()  
        add_questions(import_file)
        delfile(import_file.id)
