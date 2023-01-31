from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Category
from .serializers import (
    MakeAdvertSerializer,
    CategorySerializer
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

class GoodCategorysView(APIView):
    def get(self,request):
        categorys = Category.objects.filter(parent__isnull=True)
        srz_data = CategorySerializer(instance=categorys,many=True)
        return Response(data=srz_data.data)
    

# TODO
# make the user and pass the phone_number to the advert data !