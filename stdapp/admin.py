from django.contrib import admin
from stdapp.models import Student
class StudentAdmin(admin.ModelAdmin):
	list_display=['Sno','Sname','Sage','Scourse']
admin.site.register(Student,StudentAdmin)