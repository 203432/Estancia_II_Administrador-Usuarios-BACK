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
class TablaProfileList(APIView):
    def get(self,request,format=None):
        queryset=TablaProfile.objects.all()
        serializer = TablaProfileSerializer(queryset,many=True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=TablaProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            validated_data = serializer.validated_data
            img = TablaProfile(**validated_data)
            # img.save()
            serializer_response = TablaProfileSerializer(img)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)