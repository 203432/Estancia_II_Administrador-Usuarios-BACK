from http.client import OK
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#Importación Json
import json


# Create your views here.
#Importación de Modelos
from AdministradorRutas.models import Rutas

#Importación de Serializadors
from AdministradorRutas.serializers import rutasSerializers



class routesList(APIView):
    
    def response_Custom(self, message, data, status  ): 
        responseCustom = {"messages": "success", "payload": data, "status": status}
        responsJ=json.dumps(responseCustom)
        responseOK = json.loads(responsJ)
        return responseOK

    def get(self, request, format=None):
        queryset = Rutas.objects.all()
        serializer = rutasSerializers(queryset,many=True,context={'request':request})
        responseOK = self.response_Custom("message", serializer.data, status.HTTP_200_OK)
        return Response(responseOK)

    def post(self, request, format=None): 
        serializer = rutasSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED) 
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)  
    
