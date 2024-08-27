from django.shortcuts import render,redirect
from stdapp.models import Student
from stdapp.forms import StudentForm
import csv
from django.http import HttpResponse
def home(request):
	stud=Student.objects.all()
	return render(request,'apps/home.html',{'S':stud})
def forms(request):
	form=StudentForm()
	if request.method=="POST":
		form=StudentForm(request.POST)
	if form.is_valid():
		form.save()
	return render(request,'apps/form.html',{'form':form})

def delete(request,id):
	j=Student.objects.get(id=id)
	j.delete()
	return redirect('/result/')

def update(request,id):
	sttudent=Student.objects.get(id=id)
	if request.method=="POST":
		form=StudentForm(request.POST, instance=sttudent)
		if form.is_valid():
			form.save()
		return redirect('/result/')
	return render(request,'apps/update.html',{'s':sttudent})
def indexx(request):
	return render(request,'apps/index.html')
	
def about(request):
	return render(request,'apps/about.html')

def file(request):
	response=HttpResponse(content_type='text/csv')
	response['content_type']='attachment;filename=student.csv'
	std=Student.objects.all()
	writer=csv.writer(response)
	writer.writerow(['NO','NAME','AGE','COURSE'])
	for i in std:
		writer.writerow([i.Sno,i.Sname,i.Sage,i.Scourse])
	return response



