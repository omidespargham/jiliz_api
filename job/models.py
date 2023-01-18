from django.db import models
from advert.models import City,Category

GENDER_CHOISES = ( # جنسیت
    ("آقا","آقا"),
     ("خانوم","خانوم"),  
)
LEVEL_CHOISES = (
    ("مبتدی","مبتدی"),
     ("نیمه ماهر","نیمه ماهر"),
      ("ماهر","ماهر"),
       ("حرفه ای","حرفه ای"),
)
        
TIME_TO_WORK_CHOISES = (
    ("تمام وقت","تمام وقت"),
     ("پاره وقت","پاره وقت"),
     
)
class JobExpertise(models.Model):
    name = models.CharField(max_length=40)

class JobSeeker(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOISES)
    expertise = models.ManyToManyField(JobExpertise) # تخصص
    level = models.CharField(max_length=30,choices=LEVEL_CHOISES) # وضعیت / سطح
    time_to_work = models.CharField(max_length=30,choices=TIME_TO_WORK_CHOISES) # ساعت کاری
    city = models.ForeignKey(City,on_delete=models.SET_NULL,blank=True,null=True)
    phone = models.CharField(max_length=12)
    description = models.TextField()


#  TODO
# jobseeker model 
# محل خواب
# بیمه
# سابقه مورد نیاز
# category should be many to many field

