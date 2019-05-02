from django.shortcuts import render,redirect

from teacher.forms import  *
from teacher.models import *
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
class SurveyClass(object) :
  questions = 0
  survey = 0
  def __init__ (self,id):
    id = int(id)
    if id==0 :
      self.survey_form = SurveyForm()
    else :
      self.set_survey(id)
  
  def set_survey(self,id) :
    self.survey = Survey.objects.get(id=id)
    self.survey_form = SurveyForm(instance=self.survey)
    self.questions = Question.objects.filter(survey__id=id).order_by("page","sequence")

