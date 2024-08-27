from django.db import models

class Student(models.Model):
	Sno=models.IntegerField()
	Sname=models.CharField(max_length=24)
	Sage=models.IntegerField()
	Scourse=models.CharField(max_length=54)
# Create your models here.
