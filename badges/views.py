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
# Create your views here.
class BadgesList(APIView):
    def get(self,request,format=None):
        queryset=Badges.objects.all()
        serializer = BadgeSerializer(queryset,many=True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=BadgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            validated_data = serializer.validated_data
            img = Badges(**validated_data)
            # img.save()
            serializer_response = BadgeSerializer(img)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)