from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
from .models import *
from .serializers import *



class TypeAPI(APIView):
     def get(self, request):
          try:
                type  = TourType.objects.all()
                serializer = TourTypeSerializer(type, many=True)
                return Response({"data":serializer.data})

          except Exception as e:
                    print(e)

          return Response({"status":status.HTTP_404_NOT_FOUND})



class TagsTypeAPI(APIView):
     def get(self, request):
          try:
                type  = TagsType.objects.all()
                serializer = TagsTypeSerializer(type, many=True)
                return Response({"data":serializer.data})

          except Exception as e:
                    print(e)

          return Response({"status":status.HTTP_404_NOT_FOUND})