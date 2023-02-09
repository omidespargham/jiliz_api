from django.shortcuts import render
from rest_framework.views import APIView
from .models import student,One
from rest_framework.response import Response
from .serializer import studentserializer
from .serializers import OneSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin

class returnthestudentview(APIView):
    def get(self,request):
        students = student.objects.all()
        students_srz = studentserializer(instance=students,many=True)
        return Response(data=students_srz.data)

    def post(self,request):
        stu_data = studentserializer(data=request.data)
        if stu_data.is_valid():
            valided = stu_data.validated_data
            obj = student.objects.create(name=valided["name"])
            obj.teacher.set(valided['teacher'])
            return Response(data=stu_data.data)
        return Response(data=stu_data.errors)


class OneView(APIView):
    def get(self,request):
        ones = One.objects.all()
        ones_srz = OneSerializer(instance=ones,many=True)
        return Response(data=ones_srz.data)
    def post(self,request):
        one_srz = OneSerializer(data=request.data)
        if one_srz.is_valid():
            one_srz.save()
            return Response(one_srz.validated_data)
        return Response(one_srz.errors)

class CreateOneView(CreateAPIView):
    serializer_class = OneSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

# class createstudentview(APIView):




