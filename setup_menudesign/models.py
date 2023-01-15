from django.db import models
from django.contrib.auth import get_user_model
from jilizv3.advert.models import Category, City

User = get_user_model()
SETUP_MENUDESIGN_EXPERTISE_CHOISES = (
    ("طراحی منوی", "طراحی منوی"),
    ("راه اندازی", "راه اندازی"),
    # ("طراحی منو و راه اندازی رستوران", "طراحی منو و راه اندازی رستوران"),
    # ("طراحی منوی کافی شاپ", "طراحی منوی کافی شاپ"),
    # ("راه اندازی کافی شاپ", "راه اندازی کافی شاپ"),
    # ("طراحی منو و راه اندازی کافی شاپ", "طراحی منو و راه اندازی کافی شاپ"),
)


class SetupMenuExpertiseArea(models.Model):
    name = models.CharField(max_length=255)


class SetupMenuDesign(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="setup_menu_desgins")
    title = models.CharField(max_length=80)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    expertise_area = models.ForeignKey(SetupMenuExpertiseArea, on_delete=models.SET_NULL, null=True, blank=True) # حوزه تخصص
    expertise = models.CharField(max_length=50, choices=SETUP_MENUDESIGN_EXPERTISE_CHOISES) # تخصص
    have_guarantee = models.BooleanField()
    description = models.TextField()

    class ContractType(models.TextChoices): # نوع قرارداد
        mahzari = 'رسمی / محضری', 'رسمی / محضری'
        agreement = 'غیر رسمی / توافقی', 'غیر رسمی / توافقی'
        peyman = 'پیمان مدیریت', 'پیمان مدیریت'

    contract_type = models.CharField(max_length=30, choices=ContractType.choices, blank=False, null=False)

    class ActivityType(models.TextChoices): # نوع فعالیت
        official = 'رسمی', 'رسمی'
        unofficial = 'غیر رسمی', 'غیر رسمی'

    activity_type = models.CharField(max_length=30, choices=ActivityType.choices, blank=False, null=False)


# TODO
# سابقه فعالیت
# تحصیلات
# images
# Create your models here.
