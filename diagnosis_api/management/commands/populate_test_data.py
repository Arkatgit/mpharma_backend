from django.core.management.base import BaseCommand
from diagnosis_api.models import DiagnosisCategory ,  Diagnosis
import pandas as pd
import os
import csv
from os.path import dirname, abspath

class Command(BaseCommand):

    def handle(self, *args, **options):
        app_root  = dirname(dirname(dirname(abspath(__file__) )))
        test_file_directory  =  os.path.join(app_root , 'test_data')
        category_test_file  =  os.path.join(test_file_directory , 'categories.csv')
        diagnosis_test_file  =  os.path.join(test_file_directory, 'codes.csv' )


        category_test_file_df  =  pd.read_csv(category_test_file , header=None , names= ['category_code' , 'category_title'])

        category_test_file_df_cleaned  = category_test_file_df[ category_test_file_df.category_code != '']

        category_test_file_df_cleaned  = category_test_file_df_cleaned.drop_duplicates()

        category_test_file_df_cleaned = category_test_file_df_cleaned.drop_duplicates(subset=['category_code'], keep='first')


        s = [DiagnosisCategory(category_code=record.category_code , category_title=record.category_title) for record in category_test_file_df_cleaned.itertuples() ]
        DiagnosisCategory.objects.bulk_create(s)



        names  = ['category_code' , 'diagnosis_code' , 'full_code', 'abbreviated_description' , 'full_description' , 'category_title']
        diagnosis_test_df  = pd.read_csv(diagnosis_test_file , header=None , names= names)
        del diagnosis_test_df['category_title']

        diagnosis_test_df = diagnosis_test_df.drop_duplicates(subset= ['full_code'] , keep='first')

        diagnosis_set = []
        for index , record in diagnosis_test_df.iterrows() :
            try :
                category  =  DiagnosisCategory.objects.get(category_code = record['category_code'])

            except DiagnosisCategory.DoesNotExist:
                continue


            diagnosis_set.append(Diagnosis(full_code = record['full_code'] ,diagnosis_code =  record['diagnosis_code'],
            category_code = category, abbreviated_description = record['abbreviated_description'] ,
            full_description = record['full_description']  )  )

        Diagnosis.objects.bulk_create(diagnosis_set)
