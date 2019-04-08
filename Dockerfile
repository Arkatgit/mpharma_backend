FROM python:3.6


ENV PYTHONUNBUFFERED 1


#RUN apk upgrade --update && apk add --no-cache python3 python3-dev gcc gfortran freetype-dev musl-dev libpng-dev g++ lapack-dev


RUN mkdir /mpharma_api


WORKDIR /mpharma_api


ADD . /mpharma_api/


RUN pip install -r requirements.txt
