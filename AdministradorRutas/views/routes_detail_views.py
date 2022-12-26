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




class routesDetail(APIView):
    def get_object(self, pk):
        try:
            return Rutas.objects.get(pk = pk)  
        except Rutas.DoesNotExist:   
            return 0
    
    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = rutasSerializers(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)    

    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        serializer = rutasSerializers(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED) 
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)   

            
    def delete(self, request, pk, format=None):
        objetive = self.get_object(pk)
        if objetive!="No existe":
            objetive.delete()
            return Response("Ruta eliminada",  status = status.HTTP_200_OK)
        else:
            return Response("Ruta no encontrada", status = status.HTTP_400_BAD_REQUEST)