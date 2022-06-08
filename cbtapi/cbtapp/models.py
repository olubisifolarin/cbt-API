from tkinter import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import *
# from django.utils.text import slugify



# Create your models here.
    
class Question(models.Model):
    ques = models.CharField(max_length=100)
    # answer = models.ForeignKey('Answer', on_delete=models.CASCADE)
    a = models.CharField(max_length=50)
    b = models.CharField(max_length=50)
    c= models.CharField(max_length=50)
    d = models.CharField(max_length=50)
   
    def __str__(self):
        return self.ques
    

class Answer(models.Model):
  
    ans = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.ans
    
