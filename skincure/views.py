from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Treatment, SkinDisease
from .serializers import SkinDiseaseSerializer, TreatmentSerializers
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
# Create your views here.

class TreatmentViewSet(ListCreateAPIView):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializers
    
class TreatmentRetrieveViewSet(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializers
    
class SkinDiseaseViewSet(ListCreateAPIView):
    queryset = SkinDisease.objects.all()
    serializer_class = SkinDiseaseSerializer
    
class SkinDiseaseRetrieveViewSet(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = SkinDisease.objects.all()
    serializer_class = SkinDiseaseSerializer