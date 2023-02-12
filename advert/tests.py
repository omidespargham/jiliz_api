from django.test import TestCase
from advert.models import Category,Advert
from advert.views import MakeAdvert
from django.urls import resolve,reverse

# this test class is for testing default database and its not real test for 
# this app
class TestMakeAdvert(TestCase):
    def setUp(self):
        Category.objects.create(name="testcategory")

    def test_can_make_advert(self):
        try:
            a = Advert.objects.create(title="title",description="description",phone_number="0912")
            a.categorys.set(Category.objects.all())
            self.assertTrue(True)
        except:
            self.assertTrue(False,msg="nemitavanim advert ra besazim")

class TestUrls(TestCase):
    def test_make_advert_url(self):
        url = reverse("advert_v1:make_advert") # /advert/v1/make-advert/
        print(url)
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class,MakeAdvert)

# Create your tests here.
