import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import  CategorySerializer
from .models import (
    Advert,
    Category,
    Brand,
    Country,
    City,

)
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .serializers import (
    ShowAdvertSerializer,
    MakeAdvertSerializer,
    MultiSearchSerializers

)
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class ShowAdvertApiView(APIView):
    def get(self, request, slug):
        get_object_or_404(Advert, slug=slug)
        obj = Advert.objects.get(slug=slug)
        serializer = ShowAdvertSerializer(instance=obj)
        return Response({'obj': serializer.data})


class MakeAdverb(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MakeAdvertSerializer(data=request.POST)

        if serializer.is_valid():
            serializer.save(category=serializer.validated_data['category'], city=serializer.validated_data['city'],
                            brand=serializer.validated_data['brand'], country=serializer.validated_data['country'])
            return Response({'ok', 'Dreams for ever'})

        return Response({'error': serializer.errors})


class SearchDataView(APIView):
    def get(self, request):
        load_all_categories = Category.objects.filter(parent__isnull=True)
        categories = []

        for category in load_all_categories:
            category_data = {'name': category.name}
            categories.append(category_data)
        return Response({'categories': categories})





class DetailCategoryView(APIView):
    def get(self, request, category):
        category = get_object_or_404(Category, name=category)
        srz_data = CategorySerializer(instance=category.get_children(), many=True)
        return Response(data={'products': srz_data.data})

        # data_cat = []
        # get_object_or_404(Category, name=category)
        # get_obj = Category.objects.get(name=category)
        #
        # get_child = get_obj.get_children()
        #
        # load_all_categories = Category.objects.filter(parent__isnull=True)
        #
        # categories = []
        #
        # for item in get_child:
        #     get_categories = Category.objects.filter(parent=item)
        #     for item2 in get_categories:
        #         data = {
        #
        #             'name': item2.name
        #         }
        #
        #         data_cat.append(data)
        #
        # for category in load_all_categories:
        #     category_data = {'name': category.name}
        #     categories.append(category_data)
        #
        #
        # return Response({'product': data_cat})

class DetailSubCategoryView(APIView):
    def get(self, request, category):
        category = get_object_or_404(Category, name=category)
        categories = CategorySerializer(instance=category.get_children(),many=True).data
        if not category.is_child_node():
            data = {'zirgrooh': categories}
        else:
            data = {'products': categories}
        return Response(data=data)
        # category = Category.objects.get(name=category)
        # zirgrooh = False
        # if category.is_child_node():
        #     zirgrooh = True
        # categories = []
        # for item in category.get_children():
        #
        #     for item2 in item.get_children():
        #         data = {
        #
        #             'name': item2.name
        #         }
        #         categories.append(data)
        # if zirgrooh:
        #     data = {'zirgrooh': categories}
        # else:
        #     data = {'product': categories}
        # return Response(data=data)



        # data = []
        # get_obj = Category.objects.get(name=category)
        # get_obj_all = get_obj.get_descendants()
        #
        # for item in get_obj_all:
        #     if item.parent == get_obj:
        #         for item2 in item.get_descendants():
        #             print(item2)
        #             if item2.get_children != 1:
        #                 data2 = {
        #                     'fields': item2.name,
        #                     'childs': [i.name for i in Category.objects.filter(parent=item.id)]
        #                 }
        #                 data.append(data2)
        #     print(data)


class MultiSearchView(APIView):
    def post(self, request):
        serializer = MultiSearchSerializers(data=request.POST)

        if serializer.is_valid():
        #
        #     for item in serializer.validated_data:
        #         data2 = {item: serializer.validated_data.get(item)}
        #
        #     Advert.objects.filter(**data2)
        #     Out[4]: < QuerySet[ < Advert: This is Title >] >

            return Response({'ok': 'check the console'})