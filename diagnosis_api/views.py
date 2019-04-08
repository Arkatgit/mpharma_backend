from rest_framework import generics
from diagnosis_api.models import DiagnosisCategory , Diagnosis
from diagnosis_api.serializers import ( DiagnosisCategorySerializer , DiagnosisSerializer )
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



class DiagnosisCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = DiagnosisCategory.objects.all()
    serializer_class = DiagnosisCategorySerializer
    lookup_field  =  'category_code'



class DiagnosisViewSet(viewsets.ModelViewSet) :
    permission_classes = (IsAuthenticated,)

    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
    lookup_field = 'full_code'
