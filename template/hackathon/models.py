from django.db import models


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    context = models.CharField(max_length=30)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class SurveyResult(models.Model):
    ids = models.IntegerField()
    question = models.TextField()
    answer = models.BooleanField()
    school = models.IntegerField()
