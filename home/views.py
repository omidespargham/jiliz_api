from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import HomeCategorySerializer,HomeGetAdvertSerialiser
from advert.models import (
    Category,
    Advert
)
from django.core.cache import cache
from rest_framework.generics import GenericAPIView

# this is for 4 adverts with category view
class HomePageDataView(GenericAPIView,APIView):
    """
    this api return parent categorys with their adverts
    for home page.
    """
    serializer_class = HomeCategorySerializer
    def get(self, request):
        categorys = Category.objects.filter(parent__isnull=True)
        category_srz = HomeCategorySerializer(instance=categorys,many=True, context={'host': request.META['HTTP_HOST']})
        return Response(data=category_srz.data)


# return adverts with category 5
class HomePageCategoryDataView(GenericAPIView,APIView):
    """
    this api return adverts
    you will pass a number and category_id 
    and it will return adverts that has that category
    the number is how many adverts should return from -5 of that

    """
    serializer_class = HomeGetAdvertSerialiser
    def get(self, request, num_post, category_id):
        visble = 5
        upper = num_post
        lower = upper - visble
        get_category = Category.objects.get(id=category_id)
        load_adverts = Advert.objects.filter(categorys=get_category).order_by('-created_obj')[:upper]
        adverts_srz = HomeGetAdvertSerialiser(load_adverts,many=True).data
        return Response(adverts_srz)


# class SaveDataInCacheView(APIView):
#     def post(self,request,key,value):
#         # for key,value in request.data:
#         cache.set(key,value)

#         return Response(data={"OK":"make it as avatar !"})

# class GetDataFromCacheView(APIView):
#     def get(self,request,key):
#         result = cache.get(key,"null")
#         return Response(data={result:"you got the data !"})