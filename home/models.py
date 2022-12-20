from django.db import models


class SliderHome(models.Model):
    image0 = models.ImageField()
    image1 = models.ImageField()
    image2 = models.ImageField()