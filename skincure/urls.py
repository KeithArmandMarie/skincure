from django.urls import path
from .views import SkinDiseaseRetrieveViewSet, SkinDiseaseViewSet, TreatmentViewSet, TreatmentRetrieveViewSet
urlpatterns = [
path('treatment/', TreatmentViewSet.as_view(), name = 'treatment'),
path('treatment/<int:id>', TreatmentRetrieveViewSet.as_view(), name = 'treatment-retrieve'),
path('skindisease/', SkinDiseaseViewSet.as_view(), name = 'skindisease'),
path('skindisease/<int:id>', SkinDiseaseRetrieveViewSet.as_view(), name = 'skindisease-retrieve'),
]
