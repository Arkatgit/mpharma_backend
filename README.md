# API for Diagnostic Codes
API providing RESTful web service for handling arbitrary Diagnostic Codes


# Summary  
This is a simple REST API application providing services that allow consumers to
access resources for handling Internationalized set of Diagnosis Code.  It allows clients
to create,edit,list and retrieve diagnosis codes. The API uses JWT for authentication and runs
on a Postgress backend.  


# Clone
Clone this repo to your local machine [ Here ]( https://github.com/Arkatgit/mpharma_backend.git )  


# Set Up & Run Code  

*  Clone repo to local machine with **git clone** https://github.com/Arkatgit/mpharma_backend.git
*  **cd mpharma_backend**  
*  Implicitly build image and apply migrations with **docker-compose run web python /mpharma_api/manage.py migrate --noinput**
*  Populate database with test data with **docker-compose run web python /mpharma_api/manage.py migrate  populate_test_data**   
*  Create a createsuperuser for authentication with **docker-compose run web python /mpharma_api/manage.py createsuperuser**  
*  Run Docker container with **docker-compose up**


# Endpoints  

The application Endpoints can be accessed via a coreapi interface at  http://127.0.0.1:8000/mpharma-api/docs/

# Technologies
* Django 2.2
* Django Rest Framework(DRF)  
* PostgreSQL



# Reference  


https://en.wikipedia.org/wiki/ICD-10

https://en.wikipedia.org/wiki/International_Statistical_Classification_of_Diseases_and_Related_Health_Problems
