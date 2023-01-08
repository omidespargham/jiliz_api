from django.db import models

class teacher(models.Model):
    name = models.CharField(max_length=255)


class student(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ManyToManyField("teacher")




# Create your models here.
