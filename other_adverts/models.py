from django.db import models
from django.contrib.auth import get_user_model
from advert.models import Category,City
from mptt.models import TreeForeignKey
User = get_user_model()


class Service(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"
EDUCATION_CHOICES = ( # تحصیلات
    ("", ""),
    ("زیر دیپلم", "زیر دیپلم"),
    ("دیپلم", "دیپلم"),
    ("فوق دیپلم", "فوق دیپلم"),
    ("لیسانس", "لیسانس"),
    ("فوق لیسانس", "فوق لیسانس"),
    ("دکترا", "دکترا"),
)
     
class InstallRepairAdvert(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="InstallRepairAdverts")
    category = TreeForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    Services = models.ForeignKey(Service,on_delete=models.SET_NULL,null=True,blank=True) # خدمات
    have_guarantee = models.BooleanField(default=False)
    description = models.TextField()
    education = models.CharField(max_length=30,choices=EDUCATION_CHOICES,default="") # تحصیلات
    city = models.ForeignKey(City,on_delete=models.SET_NULL,null=True,blank=True)
    class ActivityType(models.TextChoices): # نوع فعالیت
        official = 'رسمی', 'رسمی'
        unofficial = 'غیر رسمی', 'غیر رسمی'

    user_activity_type = models.CharField(max_length=30, choices=ActivityType.choices, blank=False, null=False) # نوع فعالیت

    class UserExperience(models.TextChoices): # سابقه فعالیت
        under_one = 'زیر یکسال', 'زیر یکسال'
        oneـto_three_years = 'یک الی سه سال', 'یک الی سه سال'
        threeـto_five_years = 'سه الی پنج سال', 'سه الی پنج سال'
        fiveـto_ten_years = 'پنج الی ده سال', 'پنج الی ده سال'

    user_activity_experience = models.CharField(max_length=30, choices=UserExperience.choices, blank=False, null=False) # سابقه فعالیت

    class Expert(models.TextChoices): # تخصص
        intall = 'نصاب حرفه ای', 'نصاب حرفه ای'
        repair = 'تعمیرکار حرفه ای', 'تعمیرکار حرفه ای'
        install_repair = 'نصب و تعمیرات حرفه ای' , 'نصب و تعمیرات حرفه ای'

    user_expert = models.CharField(max_length=30, choices=Expert.choices, blank=False, null=False) # تخصص


