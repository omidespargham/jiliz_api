from django.db import models
from django.contrib.auth import get_user_model
from advert.models import Category,City
from mptt.models import TreeForeignKey
User = get_user_model()

EDUCATION_CHOICES = ( # تحصیلات
    ("", ""),
    ("زیر دیپلم", "زیر دیپلم"),
    ("دیپلم", "دیپلم"),
    ("فوق دیپلم", "فوق دیپلم"),
    ("لیسانس", "لیسانس"),
    ("فوق لیسانس", "فوق لیسانس"),
    ("دکترا", "دکترا"),
)


SETUP_MENUDESIGN_EXPERTISE_CHOISES = (
    ("طراحی منوی", "طراحی منوی"),
    ("راه اندازی", "راه اندازی"),
    ("طراحی منوی و راه اندازی", "طراحی منوی و راه اندازی"),
)


class SetupAndMenuExpertiseArea(models.Model):
    name = models.CharField(max_length=255)

 # راه اندازی و طراحی منو
class SetupMenuDesign(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="setup_menu_desgins")
    title = models.CharField(max_length=80)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    expertise_area = models.ForeignKey(SetupAndMenuExpertiseArea, on_delete=models.SET_NULL, null=True, blank=True) # حوزه تخصص
    expertise = models.CharField(max_length=50, choices=SETUP_MENUDESIGN_EXPERTISE_CHOISES) # تخصص
    have_guarantee = models.BooleanField()
    description = models.TextField()
    education = models.CharField(max_length=30,choices=EDUCATION_CHOICES,default="") # تحصیلات
    class ContractType(models.TextChoices): # نوع قرارداد
        mahzari = 'رسمی / محضری', 'رسمی / محضری'
        agreement = 'غیر رسمی / توافقی', 'غیر رسمی / توافقی'
        peyman = 'پیمان مدیریت', 'پیمان مدیریت'

    contract_type = models.CharField(max_length=30, choices=ContractType.choices, blank=False, null=False)

    class ActivityType(models.TextChoices): # نوع فعالیت
        official = 'رسمی', 'رسمی'
        unofficial = 'غیر رسمی', 'غیر رسمی'

    activity_type = models.CharField(max_length=30, choices=ActivityType.choices, blank=False, null=False)

    class UserExperience(models.TextChoices): # سابقه فعالیت
        under_one = 'زیر یکسال', 'زیر یکسال'
        oneـto_three_years = 'یک الی سه سال', 'یک الی سه سال'
        threeـto_five_years = 'سه الی پنج سال', 'سه الی پنج سال'
        fiveـto_ten_years = 'پنج الی ده سال', 'پنج الی ده سال'

    user_activity_experience = models.CharField(max_length=30, choices=UserExperience.choices, blank=False, null=False) # سابقه فعالیت


