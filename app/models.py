from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    scname=models.CharField(max_length=100)
    scloc=models.CharField(max_length=100)
    scprincipal=models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse("School_Detail",kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.scname

class Student(models.Model):
    scname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    studentname=models.CharField(max_length=100)
    stage=models.IntegerField()