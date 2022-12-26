from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asyncio import exceptions
import os.path

#Importaciones de modelos
from badges.models import Badges

#Importaciones de serializadores
from badges.serializers import BadgeSerializer




class BadgesDetail(APIView):
    def get_object(self, pk):
        try:
            return Badges.objects.get(pk = pk)  
        except Badges.DoesNotExist:   
            return 0
    
    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = BadgeSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)    

    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        serializer = BadgeSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED) 
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)   

    def patch(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        serializer = BadgeSerializer(idResponse, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED) 
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

            
    def delete(self, request, pk, format=None):
        objetive = self.get_object(pk)
        if objetive!="No existe":
            objetive.delete()
            return Response("Insignia eliminada",  status = status.HTTP_200_OK)
        else:
            return Response("Insignia no encontrada", status = status.HTTP_400_BAD_REQUEST)