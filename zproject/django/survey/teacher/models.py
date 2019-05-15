from django.db import models
import datetime

# Create your models here.

class Course(models.Model) :
    department  =   models.CharField(max_length=128,blank=True)
    title       =   models.CharField(max_length=256,blank=True)
    name        =   models.CharField(max_length=256,blank=True)
    section     =   models.CharField(max_length=256,blank=True)
    instructor  =   models.CharField(max_length=256,blank=True)
  
class Survey(models.Model):
    name            =   models.CharField(max_length=256)
    requester       =   models.CharField(max_length=256)
    description     =   models.CharField(max_length=1024)
    subject         =   models.CharField(max_length=256)
    url             =   models.CharField(max_length=512,blank=True)
    locked          =   models.BooleanField(default=False)
    created         =   models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return "{}".format(self.name)

class Question(models.Model):
    survey          =   models.ForeignKey(Survey, on_delete=models.CASCADE)
    format          =   models.CharField(max_length=30,blank=True)
    question        =   models.CharField(max_length=2048)
    sequence        =   models.SmallIntegerField()
    created         =   models.DateTimeField(auto_now_add=True)

class Student(models.Model):
    survey          =   models.ForeignKey(Survey, on_delete=models.CASCADE)
    name            =   models.CharField(max_length=128)
    grade_level     =   models.CharField(max_length=4)
    test_code       =   models.CharField(max_length=32)
    created         =   models.DateTimeField(auto_now=True)

class Answer(models.Model):
    student         =   models.ForeignKey(Student, on_delete=models.CASCADE)
    course          =   models.ForeignKey(Course, on_delete=models.CASCADE)
    question        =   models.ForeignKey(Question, on_delete=models.CASCADE)
    answer          =   models.CharField(max_length=10)

class ImportFile(models.Model):
    document      = models.FileField(upload_to='uploads/' )
    created       = models.DateTimeField(auto_now_add=True)

