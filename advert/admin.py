from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.City)
admin.site.register(models.Country)
admin.site.register(models.Brand)
admin.site.register(models.Advert)


