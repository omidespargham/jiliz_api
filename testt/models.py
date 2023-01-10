from django.db import models

class teacher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
        
class student(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ManyToManyField("teacher",related_name="students")

    def __str__(self):
        return f"{self.name}"



# Create your models here.
