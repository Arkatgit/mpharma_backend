from django.db import models


class DiagnosisCategory(models.Model) :
     category_code   =   models.CharField( max_length = 10 ,  unique=True)
     category_title  =   models.CharField( max_length = 300)
     created    =  models.DateTimeField(auto_now_add=True)
     updated  = models.DateTimeField(auto_now=True)

     class Meta :
         def __str__(self) :
             return "%s  %s"  %( category_code ,  category_title)


class Diagnosis(models.Model) :
    CODE_CHOICES = (
                       ( 'ICD_10'  ,  'icd-10') ,
                       ( 'ICD_9' ,  'icd-9'),
    )


    diagnosis_code_type   =   models.CharField( max_length=10 , choices=CODE_CHOICES , default = CODE_CHOICES[0][0] )
    diagnosis_code  =  models.CharField( max_length=15)
    full_code  =  models.CharField(max_length=20 , unique=True)
    abbreviated_description =  models.CharField( max_length = 400)
    full_description  = models.CharField(max_length = 500)
    created    =  models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    category_code  =  models.ForeignKey( DiagnosisCategory , related_name="diagnosis_category" , on_delete=models.CASCADE )

    class Meta:
        ordering  = ('diagnosis_code_type' , 'full_code')

        def __str__(self) :
            return "%s  %s %s  %s  %s" %( diagnosis_code , full_code ,  abbreviated_description , full_destination , diagnosis_code_type)
