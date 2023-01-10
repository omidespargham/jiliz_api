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
    user = models.ForeignKey(USER, on_delete=models.CASCADE, null=True, blank=True)
    category = TreeForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True,related_name="adverts")
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.CharField(max_length=100,null=True,blank=True)
    agreement_price = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=12)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    # expired
    publish = models.BooleanField(default=False, verbose_name='وعضیت آگهی')
    slug = models.SlugField(blank=True, null=True, unique=True, editable=False)
    brand = models.ForeignKey('Brand', to_field='name', blank=True, null=True, on_delete=models.CASCADE, default='نامعلوم')
    country = models.ForeignKey('Country', to_field='name',blank=True, null=True, on_delete=models.CASCADE, default='نامعلوم')
    image0 = models.ImageField(blank=True, null=True, upload_to='adverts_images/', default='defaults/default-thumbnail.jpg')
    image1 = models.ImageField(blank=True, null=True, upload_to='adverts_images/', default='defaults/default-thumbnail.jpg')
    image2 = models.ImageField(blank=True, null=True, upload_to='adverts_images/', default='defaults/default-thumbnail.jpg')
    image3 = models.ImageField(blank=True, null=True, upload_to='adverts_images/', default='defaults/default-thumbnail.jpg')
    image4 = models.ImageField(blank=True, null=True, upload_to='adverts_images/', default='defaults/default-thumbnail.jpg')
    image5 = models.ImageField(blank=True, null=True, upload_to='adverts_images/', default='defaults/default-thumbnail.jpg')
    addres = models.TextField(blank=False, null=False)
    created_obj = models.DateTimeField(auto_now_add=True, editable=False)
    
    class Advertstatus(models.TextChoices):
        New = 'new', 'نو'
        Worked = 'worked', 'کارکرده'

    status_type = models.CharField(max_length=30, choices=Advertstatus.choices, blank=False, null=False)

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
    state = models.CharField(_('state'), max_length=80)

    def __str__(self):
        return str(self.name_city)





class Category(MPTTModel):
    name = models.CharField(max_length=90)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')



    class MPTTMeta:
        verbose_name = 'دسته بندی ها '

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)


    def __str__(self):
        return str(f'Country {self.name}')



class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(f'Brand {self.name}')