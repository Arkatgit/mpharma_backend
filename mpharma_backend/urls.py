from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mpharma-api/' , include('diagnosis_api.urls' ,  namespace="diagnosis_api") ) ,
    path('mpharma-api/docs/', include_docs_urls(title='Mpharm Diagnosis Api')) ,
]
