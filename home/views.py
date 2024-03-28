from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView, Response
from .models import Opinion, DataImage
from .serializers import OpinionSerializer, DataImageSerializer
from rest_framework import status



class OpinionAPI(ListAPIView):
     queryset = Opinion.objects.all()
     serializer_class = OpinionSerializer



class DataImageAPI(APIView):
     def get(self, request):
         try:
             date = DataImage.objects.all()
             serializer = DataImageSerializer(date, many=True, context={'request': self.request})
             return Response({"data":serializer.data})

         except Exception as e:
              print(e)

         return  Response({"status":status.HTTP_404_NOT_FOUND})
