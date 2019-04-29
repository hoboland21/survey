from django.shortcuts import render,redirect


from teacher.forms import ImportFileForm, SurveyForm, LayoutForm
from teacher.models import ImportFile , Survey, Question, Layout, Items
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
#------------------
class SurveyClass(object) :
  layout = 0
  questions = 0
  layouts = 0
  survey = 0
  def __init__ (self,id):
    id = int(id)
    if id==0 :
      self.survey_form = SurveyForm()
    else :
      self.set_survey(id)
      self.layouts = Layout.objects.filter(survey__id=id)
      self.survey_form = SurveyForm(instance=self.survey)
  
  def set_survey(self,id) :
    self.survey = Survey.objects.get(id=id)
  
  def set_layout(self,id) :
    if id == 0 :
      self.layout_form = LayoutForm()
    else:
      self.layout =  Layout.objects.get(id=id)
      self.layout_form = LayoutForm(instance=self.layout)
      self.questions = Items.objects.filter(layout__id=id)




