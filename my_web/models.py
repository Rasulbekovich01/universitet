from django.db import models

# Create your models here.



class Faculty(models.Model):
    name = models.CharField(max_length=100)
    dean = models.ForeignKey()

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey()
    head = models.ForeignKey()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    faculty = models.ForeignKey()
    department = models.ForeignKey()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    description = models.TextField()
    credits = models.IntegerField()
    department = models.ForeignKey()
    teacher = models.ForeignKey()

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    enrollment_date = models.DateField()
    faculty = models.ForeignKey()
    department = models.ForeignKey()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
