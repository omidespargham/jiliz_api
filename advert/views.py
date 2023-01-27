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

# in view baraye return subcategory haye yek category ast(garm,srd,...).
class DetailCategoryView(APIView):
    def get(self, request, category):
        category = get_object_or_404(Category, name=category)
        srz_data = CategorySerializer(instance=category.get_children(), many=True)
        return Response(data={'products': srz_data.data})

# in view baraye return subcategory hay ya zir grouh haye category khadamati ast.
class DetailSubCategoryKhadamatiView(APIView):
    def get(self, request, category):
        category = get_object_or_404(Category, name=category)
        categories = CategorySerializer(instance=category.get_children(),many=True).data
        if not category.is_child_node():
            data = {'zirgrooh': categories}
        else:
            data = {'products': categories}
        return Response(data=data)



class MakeAdverb(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MakeAdvertSerializer(data=request.data)

        if serializer.is_valid():
            valided = serializer.validated_data
            valided["user"] = request.user
            # TODO 
            # make the user and pass the phone_number to the advert data !
            valided["phone_number"] = request.user.phone_number
            serializer.create(valided)
            return Response({'ok':'make it as avatar ;)'})

        return Response(data=serializer.errors)



# should be check 

class ShowAdvertApiView(APIView):
    def get(self, request, slug):
        get_object_or_404(Advert, slug=slug)
        obj = Advert.objects.get(slug=slug)
        serializer = ShowAdvertSerializer(instance=obj)
        return Response({'obj': serializer.data})


class SearchDataView(APIView):
    def get(self, request):
        load_all_categories = Category.objects.filter(parent__isnull=True)
        categories = []

        for category in load_all_categories:
            category_data = {'name': category.name}
            categories.append(category_data)
        return Response({'categories': categories})






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


# TODO
# make the user and pass the phone_number to the advert data !