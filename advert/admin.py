from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin


class CityAdmin(admin.ModelAdmin):
    list_display = ("name_city","id")

class BrandAdmin(admin.ModelAdmin):
    list_display = ("name","id")

class CountryAdmin(admin.ModelAdmin):
    list_display = ("name","id")

class AdvertAdmin(admin.ModelAdmin):
    list_display = ("title","id")

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.City,CityAdmin)
admin.site.register(models.Country,CountryAdmin)
admin.site.register(models.Brand,BrandAdmin)
admin.site.register(models.Advert,AdvertAdmin)



