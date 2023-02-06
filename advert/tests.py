from django.test import TestCase
from advert.models import Category,Advert


# this test class is for testing default database and its not real test for 
# this app
class TestMakeAdvert(TestCase):
    def setUp(self):
        Category.objects.create(name="testcategory")
    def test_can_make_advert(self):
        try:
            Advert.objects.create(title="title",description="description",agreement_price=True,phone_number="0912")
            self.assertTrue(True)
        except:
            self.assertTrue(False,msg="nemitavanim advert ra besazim")


# Create your tests here.
