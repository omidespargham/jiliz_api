from django.shortcuts import render
from rest_framework.views import APIView
from .models import student
from rest_framework.response import Response
from .serializer import studentserializer


class returnthestudentview(APIView):
    def get(self,request):
        students = student.objects.all()
        students_srz = studentserializer(instance=students,many=True)
        return Response(data=students_srz.data)

    def post(self,request):
        stu_data = studentserializer(data=request.data)
        if stu_data.is_valid():
            valided = stu_data.validated_data
            student.objects.create(name=valided["name"],teacher=valided['teacher'])
            return Response(data=stu_data.data)
        return Response(data=stu_data.errors)


# class createstudentview(APIView):




