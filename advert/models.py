from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from abc import abstractmethod
import uuid
from mptt.models import MPTTModel, TreeForeignKey,TreeManyToManyField




USER = get_user_model()




class Advert(models.Model):
    user = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True) # we will set
    categorys = TreeManyToManyField('Category',related_name="adverts")# required
    title = models.CharField(max_length=50) # required
    description = models.TextField() # required
    price = models.CharField(max_length=100,blank=True)
    # agreement_price = models.BooleanField() # tavafoghi(True) gheymat(False) # required
    phone_number = models.CharField(max_length=12) # we will set
    city = models.ForeignKey('City', on_delete=models.SET_NULL,null=True) # required
    # expired
    publish = models.BooleanField(default=False, verbose_name=' نمایش آگهی') # we will set
    slug = models.SlugField(unique=True, editable=False) # we will set
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL,null=True)
    image0 = models.ImageField(blank=True, null=True, upload_to='adverts_images/', default='defaults/default-thumbnail.jpg') # required
    image1 = models.ImageField(blank=True, null=True, upload_to='adverts_images/', default='defaults/default-thumbnail.jpg')
    image2 = models.ImageField(blank=True, null=True, upload_to='adverts_images/', default='defaults/default-thumbnail.jpg')
    image3 = models.ImageField(blank=True, null=True, upload_to='adverts_images/', default='defaults/default-thumbnail.jpg')
    image4 = models.ImageField(blank=True, null=True, upload_to='adverts_images/', default='defaults/default-thumbnail.jpg')
    image5 = models.ImageField(blank=True, null=True, upload_to='adverts_images/', default='defaults/default-thumbnail.jpg')
    address = models.TextField(blank=True) # required
    created_obj = models.DateTimeField(auto_now_add=True, editable=False) # we will set
    country_made_by = models.ForeignKey('Country',on_delete=models.CASCADE,null=True)
    class Advertstatus(models.TextChoices):
        New = 'نو', 'نو'
        Worked = 'کارکرده', 'کارکرده'

    status_type = models.CharField(max_length=30, choices=Advertstatus.choices, blank=False, null=False) # required

    def __str__(self):
        return str(self.title)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.id:
            self.slug = uuid.uuid4().hex[:9]
        super(Advert, self).save()


class City(models.Model):
    name_city = models.CharField(_('name city'), max_length=80, unique=True)

    def __str__(self):
        return str(self.name_city)





class Category(MPTTModel):
    name = models.CharField(max_length=90)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    class Advertstatus(models.TextChoices):
        good_category = "good_category", 'گروه کالایی'
        service_category = 'service_category', 'گروه خدمات'

    category_type = models.CharField(max_length=30, choices=Advertstatus.choices,default="good_category") # required


    class MPTTMeta:
        verbose_name = 'دسته بندی ها '

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)


    def __str__(self):
        return str(f'{self.name}')



class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(f' {self.name}')