from django.shortcuts import render,redirect


from teacher.forms import ImportFileForm, SurveyForm
from teacher.models import ImportFile , Survey, Question, Layout
import re
import csv

#------------------
def csv_read(file) :
	csv_bin = []
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader :
			csv_bin.append(row)
	return csv_bin
#------------------

def screate(request) :
    result = {}
    result["filelist"] = ImportFile.objects.all()
    result["survey"] = SurveyForm()
    if("rm" in request.POST) :
        dobj = ImportFile.objects.get(id=request.POST["rmdb"])
        os.remove(dobj.document.path)
        dobj.delete()
    return render(request,'manager/screate.html',context=result)
#------------------



def upload_file(request) :
  result = {}
  if request.method == 'POST':
    form = ImportFileForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('welcome')

  else:
      form = ImportFileForm()
  return render(request, 'manager/upload.html', {'form': form})


