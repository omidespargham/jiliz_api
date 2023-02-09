from rest_framework import serializers




class AdvertSearchSerializer(serializers.Serializer):
    categorys = serializers.IntegerField(required=False)
    title = serializers.CharField(required=True,allow_blank=True)
    # description = serializers.CharField(required=True)
    brand = serializers.IntegerField(required=False)

    


