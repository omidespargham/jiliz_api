import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from advert.serializers import HomeCategorySerializer,GetAdvertSerialiser,CitySerializer,CategorySerializer
from advert.models import (
    Category,
    City,
    Advert
)

class HomePageSearchView(APIView):
    def get(self, request):
        load_all_cities = City.objects.all()
        load_all_categories = Category.objects.filter(parent__isnull=True)
        cities = CitySerializer(instance=load_all_cities,many=True).data
        categories = CategorySerializer(instance=load_all_categories,many=True).data

        return Response({'cities': cities, 'categories': categories})

# class HomePageAllCategoriesView(APIView):

#     def get(self, request, num_post):
#         visble = 25
#         upper = num_post
#         lower = upper - visble

#         load_averts = Advert.objects.filter().order_by('-created_obj')
#         adverts_srz = GetAdvertSerialiser(load_adverts,many=True).data
#         return Response(adverts_srz)

class HomePageDataView(APIView):
    def get(self, request):
        categorys = Category.objects.filter(parent__isnull=True)
        category_srz = HomeCategorySerializer(instance=categorys,many=True, context={'host': request.META['HTTP_HOST']})
        return Response(data=category_srz.data)

class HomePageCategoryDataView(APIView):
    def get(self, request, num_post, category_id):
        visble = 5
        upper = num_post
        lower = upper - visble
        get_category = Category.objects.get(id=category_id)
        load_adverts = Advert.objects.filter(category=get_category).order_by('-created_obj')[:upper]
        adverts_srz = GetAdvertSerialiser(load_adverts,many=True).data
        return Response(adverts_srz)


