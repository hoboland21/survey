from django.db import models
import datetime

# Create your models here.


class Question(models.Model):
    question_type   =   models.CharField(max_length=30,blank=True)
    question        =   models.CharField(max_length=2048)
    label           =   models.CharField(max_length=120,blank=True)
    group           =   models.CharField(max_length=120,blank=True)
    created         =   models.DateTimeField(auto_now_add=True)

class Survey(models.Model):
    name            =   models.CharField(max_length=256)
    requester       =   models.CharField(max_length=256)
    description     =   models.CharField(max_length=1024)
    subject         =   models.CharField(max_length=256)
    label           =   models.CharField(max_length=120,blank=True)
    group           =   models.CharField(max_length=120,blank=True)
    created         =   models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return "{} -- {}".format(self.name,self.label)

class Layout(models.Model):
    survey          =   models.ForeignKey(Survey, on_delete=models.CASCADE)
    version         =   models.CharField(max_length=1024)
    description     =   models.CharField(max_length=1024)
    designer        =   models.CharField(max_length=128)
    label           =   models.CharField(max_length=120,blank=True)
    group           =   models.CharField(max_length=120,blank=True)
    created         =   models.DateTimeField(auto_now=True)

class Items(models.Model):
    layout          =   models.ForeignKey(Layout, on_delete=models.CASCADE)
    label           =   models.CharField(max_length=120,blank=True)
    group           =   models.CharField(max_length=120,blank=True)
    question        =   models.ForeignKey(Question, on_delete=models.CASCADE)
    sequence        =   models.SmallIntegerField()
    page            =   models.SmallIntegerField(default=1)

class Student(models.Model):
    layout          =   models.ForeignKey(Layout, on_delete=models.CASCADE)
    group           =   models.CharField(max_length=120,blank=True)
    label           =   models.CharField(max_length=120,blank=True)
    test_code       =   models.CharField(max_length=32)
    name            =   models.CharField(max_length=128)
    created         =   models.DateTimeField(auto_now=True)

class Answers(models.Model):
    student         =   models.ForeignKey(Student, on_delete=models.CASCADE)
    question        =   models.ForeignKey(Question, on_delete=models.CASCADE)
    answer          =   models.CharField(max_length=10)

class ImportFile(models.Model):
    description   = models.CharField(max_length=256, blank=True)
    document      = models.FileField(upload_to='uploads/' )
    created       = models.DateTimeField(auto_now_add=True)


  

