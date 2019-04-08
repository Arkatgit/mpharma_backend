from django.test import TestCase
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from diagnosis_api.models import (DiagnosisCategory , Diagnosis )
from diagnosis_api.serializers import (DiagnosisCategorySerializer ,  DiagnosisSerializer )
from django.test.client import RequestFactory
import json

client  = Client()

# Test Data
category_sample  = [ { 'category_code' : "A01" , 'category_title' : "Typhoid and paratyphoid fevers" } ,
                     { 'category_code' : "A00" , 'category_title' :	"Cholera" },
                     { 'category_code' : "A010" , 'category_title' : "Typhoid fever" },
                     {  'category_code' :  "A011" ,  'category_title' : "Paratyphoid fever A" } ,
                     {  'category_code' :  "A012" ,  'category_title' : "Paratyphoid fever B" } ,
                     {  'category_code' :  "A013" ,  'category_title' : "Paratyphoid fever C" } ,
                     {  'category_code' :  "A014" ,  'category_title' : "Paratyphoid fever, unspecified" },

]



diagnosis_sample  = [ {'diagnosis_code' : "0" ,  'full_code' : "A010"  , 'abbreviated_description' : "Cholera due to Vibrio cholerae 01",
                        'full_description' : 'biovar cholerae	Cholera due to Vibrio cholerae 01'} ,

                       {'diagnosis_code' : "1" ,  'full_code' : "A001 "  , 'abbreviated_description' : "Cholera due to Vibrio cholerae 0",
                                               'full_description' : 'biovar cholerae	Cholera due to Vibrio cholerae 01'} ,

                        {'diagnosis_code' : "9" ,  'full_code' : "A0109 "  , 'abbreviated_description' : "Cholera",
                                       'full_description' : 'unspecified	Cholera'} ,

                        {'diagnosis_code' : "6" ,  'full_code' : "A0116 "  , 'abbreviated_description' : "Typhoid fever",
                                       'full_description' : 'unspecified Typhoid fever'} ,

                        {'diagnosis_code' : "2" ,  'full_code' : "A0122 "  , 'abbreviated_description' : "Typhoid meningitis",
                                       'full_description' : 'unspecified	Typhoid meningitis unspecified'} ,
                        {'diagnosis_code' : "4" ,  'full_code' : "A0134"  , 'abbreviated_description' : "Typhoid fever with heart involvement",
                                       'full_description' : 'Typhoid fever with heart involvement'} ,

                        {'diagnosis_code' : "7" ,  'full_code' : "A0147"  , 'abbreviated_description' : "Typhoid fever with heart involvement",
                                       'full_description' : 'Typhoid fever with heart involvement'} ,
                            ]


def populate_test_data():
    i  = 0
    for record in category_sample:
        temp = DiagnosisCategory.objects.create(**record)
        diagnosis_sample[i]['category_code'] = temp
        i += 1

    for record in diagnosis_sample:
        Diagnosis.objects.create(**record)



class GetAllTest(TestCase):
    def setUp(self):
        populate_test_data()


    def test_get_all_diagnosis_category_list(self):
        response = client.get(reverse('diagnosis_api:diagnosis-category-list'))
        categories = DiagnosisCategory.objects.all()
        serializer = DiagnosisCategorySerializer(categories, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_diagnosis_list(self):
        response = client.get(reverse('diagnosis_api:diagnosis-list'))
        categories = Diagnosis.objects.all()
        serializer = DiagnosisSerializer(categories, many=True, context = {'request': RequestFactory().get('/')})
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleTest(TestCase):
    def setUp(self):
        populate_test_data()

    def test_get_valid_single_diagnosis_category(self):

        response = client.get(reverse('diagnosis_api:diagnosis-category-detail', kwargs={ 'category_code': category_sample[0]['category_code'] }))
        category  = DiagnosisCategory.objects.get(category_code = category_sample[0]['category_code'] )
        serializer = DiagnosisCategorySerializer(category)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_invalid_single_diagnosis_category(self):
        response = client.get(
            reverse('diagnosis_api:diagnosis-category-detail', kwargs={ 'category_code' : "A00000001"  }))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_get_valid_single_diagnosis(self):

        response = client.get(reverse('diagnosis_api:diagnosis-detail', kwargs={ 'full_code': diagnosis_sample[0]['full_code'] }))
        diagnosis  = Diagnosis.objects.get(full_code = diagnosis_sample[0]['full_code'] )
        serializer = DiagnosisSerializer(diagnosis ,context = {'request': RequestFactory().get('/')})
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_diagnosis(self):
        response = client.get(
            reverse('diagnosis_api:diagnosis-detail', kwargs={ 'full_code' : "A00000001"  }))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



class CreateNewTest(TestCase):

    def setUp(self):

        self.valid_diagnosis_category_payload  = category_sample[0]
        self.invalid_diagnosis_category_payload = { 'category_code' : "" , 'category_title' : "Typhoid and paratyphoid fevers" }

        self.valid_diagnosis_payload = diagnosis_sample[0]
        self.invalid_diagnosis_payload  = {'diagnosis_code' : "7" ,  'full_code' : ""  , 'abbreviated_description' : "Typhoid fever with heart involvement",
                       'full_description' : 'Typhoid fever with heart involvement'}


    def test_create_valid_diagnosis_category(self):
        response = client.post(
            reverse('diagnosis_api:diagnosis-category-list'),
            data=json.dumps(self.valid_diagnosis_category_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_diagnosis_category(self):
        response = client.post(
            reverse('diagnosis_api:diagnosis-category-list'),
            data=json.dumps(self.invalid_diagnosis_category_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


        def test_create_valid_diagnosis(self):
            response = client.post(
                reverse('diagnosis_api:diagnosis-list'),
                data=json.dumps(self.valid_diagnosis_payload),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        def test_create_invalid_diagnosis(self):
            response = client.post(
                reverse('diagnosis_api:diagnosis-list'),
                data=json.dumps(self.invalid_diagnosis_payload),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class UpdateSingleTest(TestCase):

    def setUp(self):

        self.diagnosis_category_1  = DiagnosisCategory.objects.create(**category_sample[0] )
        self.diagnosis_category_2 = DiagnosisCategory.objects.create(**category_sample[1])

        self.diagnosis_1 = Diagnosis.objects.create(**diagnosis_sample[0])
        self.diagnosis_2 =  Diagnosis.objects.create(**diagnosis_sample[1])

        self.valid_diagnosis_category_payload =  {  'category_code' :  "A01" ,  'category_title' : "Paratyphoid fever, unspecified" }
        self.invalid_diagnosis_category_payload = {  'category_code' :  "" ,  'category_title' : "Paratyphoid fever, unspecified" }

        self.valid_diagnosis_payload = { 'diagnosis_code' : "0" ,
                                          'full_code' : "A010"  ,
                                          'abbreviated_description' : " Typhoid fever, unspecified ",
                                          'full_description' : 'Typhoid fever, unspecified'}



        self.invalid_diagnosis_payload = { 'diagnosis_code' : "0" ,
                                          'full_code' : ""  ,
                                          'abbreviated_description' : "Cholera due to Vibrio cholerae 01",
                                          'full_description' : 'biovar cholerae	Cholera due to Vibrio cholerae 01'}


    def test_valid_update_diagnosis_category(self):
        response = client.put(
            reverse('diagnosis_api:diagnosis-category-detail' , kwargs={'category_code': self.diagnosis_category_1.category_code }),
            data=json.dumps(self.valid_diagnosis_category_payload),
            content_type='application/json'
        )


        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_invalid_update_diagnosis_category(self):
        response = client.put(
            reverse('diagnosis_api:diagnosis-category-detail', kwargs={'category_code': self.diagnosis_category_1.category_code }),
            data=json.dumps(self.invalid_diagnosis_category_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_valid_update_diagnosis(self):
        response = client.put(
            reverse('diagnosis_api:diagnosis-detail' , kwargs={'full_code': self.diagnosis_1.full_code }),
            data=json.dumps(self.valid_diagnosis_payload),
            content_type='application/json'
        )


        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_diagnosis(self):
        response = client.put(
            reverse('diagnosis_api:diagnosis-detail', kwargs={'full_code': self.diagnosis_1.full_code }),
            data=json.dumps(self.invalid_diagnosis_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)




class DeleteSingleTest(TestCase):

    def setUp(self):
        populate_test_data()


    def test_valid_delete_diagnosis_category(self):

        response = client.delete(
            reverse('diagnosis_api:diagnosis-category-detail', kwargs={'category_code': category_sample[0]['category_code']  }))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_diagnosis_category(self):
        response = client.delete(
            reverse('diagnosis_api:diagnosis-category-detail', kwargs={'category_code': "A000001" }))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_valid_delete_diagnosis(self):

        response = client.delete(
            reverse('diagnosis_api:diagnosis-detail', kwargs={'full_code': diagnosis_sample[0]['full_code']  }))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_diagnosis(self):
        response = client.delete(
            reverse('diagnosis_api:diagnosis-detail', kwargs={'full_code': "A000001" }))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
