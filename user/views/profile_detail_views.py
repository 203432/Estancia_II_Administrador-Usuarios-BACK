from django.shortcuts import render

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asyncio import exceptions
import os.path

#Importaciones de modelos
from user.models import TablaProfile

#Importaciones de serializadores
from user.serializers import TablaProfileSerializer

# Create your views here.
class TablaProfileDetail(APIView):
    def get_object(self, pk):
        try:
            return TablaProfile.objects.get(pk = pk)  
        except TablaProfile.DoesNotExist:   
            return 0
    
    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = TablaProfileSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)    

    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        serializer = TablaProfileSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED) 
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)   

    def patch(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        serializer = TablaProfileSerializer(idResponse, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED) 
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

            
    def delete(self, request, pk, format=None):
        objetive = self.get_object(pk)
        if objetive!="No existe":
            objetive.delete()
            return Response("Usuario eliminado",  status = status.HTTP_200_OK)
        else:
            return Response("Usuario no encontrado", status = status.HTTP_400_BAD_REQUEST)