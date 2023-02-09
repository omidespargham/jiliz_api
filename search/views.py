from django.shortcuts import render
from rest_framework.views import APIView
from advert.models import Advert
from rest_framework.response import Response
from .serializers import AdvertSearchSerializer
from django.db.models import Q
from home.serializers import HomeGetAdvertSerialiser 
class GoodsSearchView(APIView):
    def get(self,request):
        srz_advert = AdvertSearchSerializer(data=request.data)
        if srz_advert.is_valid():
            search = srz_advert.validated_data["search"]
            del srz_advert.validated_data["search"]
            adverts = Advert.objects.filter(Q(title__contains=search) | Q(description__contains=search),**srz_advert.validated_data)
            adverts_json = HomeGetAdvertSerialiser(instance=adverts,many=True)
            print(adverts)
            return Response(adverts_json.data)
        return Response(srz_advert.errors)
        


# from functools import reduce
# topics = reduce(lambda qs, pk: qs.filter(categorys=pk), [4,8], Advert.objects.all())
# one = Advert.objects.filter(Q(title__contains="lalo") | Q(description__contains="lalo"))