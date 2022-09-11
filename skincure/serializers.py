from rest_framework import serializers
from .models import Treatment, SkinDisease

class TreatmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ['id','description']
        
class SkinDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinDisease
        fields = ['name','id','description']
        
