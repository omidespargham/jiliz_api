from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
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



class HomePageDataView(APIView):
    def get(self, request):
        load_all_categories = Category.objects.filter(parent__isnull=True)
        product = []
        
        for category in load_all_categories:
            data = {
                'Adverts': Advert.objects.filter(category=category).order_by('created_obj').reverse()[:4],
                'category': category.name
            }  
            product.append(data)

        return Response({'products': product})