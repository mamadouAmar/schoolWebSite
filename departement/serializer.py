from rest_framework import serializers
from departement.models import DepartementModel
from rest_framework import generics

class DepartementSerializer(serializers.ModelSerializer):

    class Meta:
        model = DepartementModel
        fields ="__all__"



class ViewListDepartement(generics.ListAPIView):
    queryset = DepartementModel.objects.all()
    serialier_class = DepartementSerializer



#import requests
#req = requests.get("url")
#req.json
