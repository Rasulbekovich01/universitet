from django.contrib import admin

# Register your models here.

from .models import Faculty, Department, Teacher, Course, Student

admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Student)
