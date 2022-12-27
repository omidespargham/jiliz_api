import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from advert.serializers import HomeCategorySerializer
from advert.models import (
    Category,
    City,
    Advert
)

class HomePageSearchView(APIView):
    def get(self, request):
        load_all_cities = City.objects.all()
        load_all_categories = Category.objects.filter(parent__isnull=True)

        cities = []
        categories = []
        for city in load_all_cities:
            city_data = {'name': city.name_city}
            cities.append(city_data)
        for category in load_all_categories:
            category_data = {'name': category.name}
            categories.append(category_data)


        return Response({'cities': cities, 'categories': categories})



# class HomePageDataView(APIView):
#     def get(self, request):
#         load_all_categories = Category.objects.filter(parent__isnull=True)
#         product = []

#         for category in load_all_categories:
#             data2 = []
#             for item in Advert.objects.filter(category=Category.objects.get(parent=category.id)).order_by('created_obj').reverse()[:4]:
#                 data3 = {    #     Set good names
#                     'name': item.title,
#                     'image': item.image0.url,
#                     'price': item.price,
#                     'category': item.category.name,
#                     'slug': item.slug

#                 }
#                 data2.append(data3)

#             data = {
#                 'Adverts': data2,
#                 'category': category.name
#             }
#             product.append(data)

#         return Response({'products': product})

class HomePageDataView(APIView):
    def get(self, request):
        categorys = Category.objects.filter(parent__isnull=True)
        category_srz = HomeCategorySerializer(instance=categorys,many=True)
        return Response(data=category_srz.data)



class HomePageAllCategoriesView(APIView):

    def get(self, request, num_post):
        visble = 25
        upper = num_post
        lower = upper - visble

        load_averts = Advert.objects.filter().order_by('-created_obj')
        lst_adverts = []
        for item in load_averts:
            data = {
                'title': item.title,
                'price': item.price,
                'image': item.image0.url,
                'category': item.category.name,
                'slug': item.slug

            }
            lst_adverts.append(data)

        return Response({'data': lst_adverts[lower:upper]})


class HomePageCategoryDataView(APIView):
    def get(self, request, num_post, category):
        visble = 25
        upper = num_post
        lower = upper - visble
        get_category = Category.objects.get(name=category)
        load_averts = Advert.objects.filter(category=get_category).order_by('-created_obj')
        lst_adverts = []
        for item in load_averts:
            data = {
                'title': item.title,
                'price': item.price,
                'image': item.image0.url,
                'category': item.category.name,
                'slug': item.slug
            }
            lst_adverts.append(data)

        return Response({'data': lst_adverts[lower:upper]})


