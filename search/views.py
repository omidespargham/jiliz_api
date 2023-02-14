from django.shortcuts import render
from rest_framework.views import APIView
from advert.models import Advert
from rest_framework.response import Response
from .serializers import AdvertSearchSerializer
from django.db.models import Q
from home.serializers import HomeGetAdvertSerialiser


class GoodsSearchView(APIView):
    def get(self, request, range_number=1):
        if range_number > 0:
            range_data = range_number * 10
            srz_advert = AdvertSearchSerializer(data=request.data)
            if srz_advert.is_valid():
                query = srz_advert.make_Q_statments_for_model_querys(
                    srz_advert.validated_data)
                adverts = Advert.objects.filter(query["search"], query["category"], query["city"],
                                                query["country_made_by"], query["brand"],
                                                query["status_type"]).order_by("-created_obj")[0:range_data]
                adverts_json = HomeGetAdvertSerialiser(instance=adverts, many=True ,context={'host': request.META['HTTP_HOST']})
                return Response(adverts_json.data)
            return Response(srz_advert.errors)
        return Response({"error":"number of range should be >=1"})

# context={'host': request.META['HTTP_HOST']}

# from functools import reduce
# topics = reduce(lambda qs, pk: qs.filter(categorys=pk), [4,8], Advert.objects.all())
# one = Advert.objects.filter(Q(title__contains="lalo") | Q(description__contains="lalo"))
