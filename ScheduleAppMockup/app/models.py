"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Class(models.Model):
    title = models.CharField(max_length=25)
    department = models.CharField(max_length=4)
    level = models.CharField(max_length=4)
    period = models.IntegerField(default=0)
    instructor = models.CharField(max_length=40, blank=True, null=True)
    room = models.CharField(max_length=5)
    reddot = models.IntegerField(default=0) # 0 is no red dot, 1 is Monday, 2 Tuesday, etc.

# Represents a student
class Student(models.Model):
    user = models.OneToOneField(User, null=True)
    student_id = models.CharField(max_length=7)
    student_name = models.CharField(max_length=100)
    student_email = models.CharField(max_length=100)
    student_nickname = models.CharField(max_length=20)
    graduation_year = models.IntegerField(default=0)

class Schedule(models.Model):
    student = models.OneToOneField(Student)
    lunch_period = models.IntegerField(default=0)

    # The classes
    period1class = models.IntegerField(default=0)
    period2class = models.IntegerField(default=0)
    period3class = models.IntegerField(default=0)
    period4class = models.IntegerField(default=0)
    period5class = models.IntegerField(default=0)
    period6class = models.IntegerField(default=0)
    period7class = models.IntegerField(default=0)