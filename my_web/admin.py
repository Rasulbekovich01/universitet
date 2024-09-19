from django.contrib import admin
from .models import Faculty, Department, Teacher, Course, Student
# Register your models here.



admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Student)
