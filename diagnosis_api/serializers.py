from rest_framework import serializers
from diagnosis_api.models import (DiagnosisCategory , Diagnosis)
from diagnosis_api.models import DiagnosisCategory



class DiagnosisCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model  = DiagnosisCategory
        fields  = ( 'category_code' ,  'category_title' )
        lookup_field = 'category_code'



class DiagnosisSerializer( serializers.HyperlinkedModelSerializer) :
    category_code  = serializers.HyperlinkedRelatedField(
        view_name  = 'diagnosis_api:diagnosis-category-detail' ,
        lookup_field = "category_code" ,
        read_only=True )

    
    class Meta:
        model  = Diagnosis

        fields  = ('category_code' , 'diagnosis_code' , 'full_code' , 'abbreviated_description' ,  'full_description' )
        lookup_field = 'full_code'
