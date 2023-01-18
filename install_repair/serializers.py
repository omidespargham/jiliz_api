from rest_framework.serializers import ModelSerializer
from .models import InstallRepairAdvert


class InstallRepairMakeSerializer(ModelSerializer):
    class Meta:
        model = InstallRepairAdvert
        fields = ("category",
                  "title",
                  "Services",
                  "have_guarantee",
                
                  "description",
                  "education",
                  "city",
                #   "user_activity_type",
                #   "user_activity_experience",
                  "user_expert")

        extra_kwargs = {
            # "have_guarantee":{"required":False},
            "city": {"required": True},
            "user_activity_type": {"required": True},
            "user_activity_experience": {"required": True},
            "user_expert": {"required": True},
            "have_guarantee": {"required":True}
        }
