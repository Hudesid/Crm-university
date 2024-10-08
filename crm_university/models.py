from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, related_name='groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, related_name='students', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, related_name='subjects', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, related_name='teachers', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"