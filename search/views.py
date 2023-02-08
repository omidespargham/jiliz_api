from django.shortcuts import render
from rest_framework.views import APIView
from advert.models import Advert
# Create your views here.

class GoodsSearchView(APIView):
    def get(self,request):

        Advert.objects.filter(**request.data)
        


# from functools import reduce
# topics = reduce(lambda qs, pk: qs.filter(categorys=pk), [4,8], Advert.objects.all())
# one = Advert.objects.filter(Q(title__contains="lalo") | Q(description__contains="lalo"))