from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Category,Country,City,Brand
from .serializers import (
    MakeAdvertSerializer,
    CategorySerializer,
    CountrySerializer,
    CitySerializer,
    BrandSerializer
)
# in view baraye return subcategory haye yek category ast(garm,srd,...).
class CategoryChildsView(APIView):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        srz_data = CategorySerializer(instance=category.get_children(), many=True)
        return Response(data={'products': srz_data.data})



# in view baraye return subcategory hay ya zir grouh haye category khadamati ast.
class KhadamatiSubCategorysView(APIView):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        categories = CategorySerializer(instance=category.get_children(),many=True).data
        if not category.is_child_node():
            data = {'zirgrooh': categories}
        else:
            data = {'products': categories}
        return Response(data=data)



class MakeAdvert(APIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = MakeAdvertSerializer
    def post(self, request):
        serializer = MakeAdvertSerializer(data=request.data)

        if serializer.is_valid():
            valided = serializer.validated_data
            # valided["user"] = request.user
            # TODO
            # make the user and pass the phone_number to the advert data !
            # valided["phone_number"] = request.user.phone_number
            serializer.create(valided)
            return Response({'ok':'make it as avatar ;)'})

        return Response(data=serializer.errors)

class MakeAdvert2(CreateAPIView):
    serializer_class = MakeAdvertSerializer

    def create(self, request, *args, **kwargs):
        serializer = MakeAdvertSerializer(data=request.data)

        if serializer.is_valid():
            valided = serializer.validated_data
            # valided["user"] = request.user
            # TODO
            # make the user and pass the phone_number to the advert data !
            # valided["phone_number"] = request.user.phone_number
            serializer.create(valided)
            return Response({'ok':'make it as avatar ;)'})

        return Response(data=serializer.errors)
        # return super().create(request, *args, **kwargs)

class GoodCategorysView(APIView):
    def get(self,request):
        categorys = Category.objects.filter(parent__isnull=True)
        srz_data = CategorySerializer(instance=categorys,many=True)
        return Response(data=srz_data.data)

class CountrysMakeByView(APIView):
    def get(self,request):
        countrys = Country.objects.all()
        country_srz = CountrySerializer(instance=countrys,many=True)
        return Response(data=country_srz.data)

class CityView(APIView):
    def get(self,request):
        citys = City.objects.all()
        citys_srz = CitySerializer(instance=citys,many=True)
        return Response(data=citys_srz.data)

class BrandView(APIView):
    def get(self,request):
        brands = Brand.objects.all()
        brands_srz = BrandSerializer(instance=brands,many=True)
        return Response(data=brands_srz.data)

# TODO
# make the user and pass the phone_number to the advert data !