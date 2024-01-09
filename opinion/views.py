from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView

from  django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class AbroadAPI(ModelViewSet):
     serializer_class = TravelSerializer



     def get_queryset(self):
         if 'language_code' in self.request.GET:
               language_code = self.request.GET.get('language_code')
               queryset = Tour.objects.language(language_code).order_by('-id')
         else:
               queryset = Tour.objects.language().order_by('id')
         return queryset


class InformationAPI(APIView):
     def get(self, request, pk=None):
          try:
              info = Tour.objects.get(id=pk)
              serializers = InformationSerializer(info)
              return Response({"data":serializers.data})

          except Exception as e:
                    print(e)

          return  Response({"status":status.HTTP_404_NOT_FOUND})



class AbroadGalleryAPI(APIView):
     def get(self, request, pk):
          try:
             tour = Tour.objects.get(id=pk)
             serializers = GallerySerializer(tour,context={"request": self.request})
             return Response({"data":serializers.data})
          except Exception as e:
               print(e)

          return Response({"status":status.HTTP_404_NOT_FOUND})



# class AbroadInformationAPI(ModelViewSet):
#       serializer_class = InformationSerializer
#
#       def get_queryset(self):
#           if 'language_code' in self.request.GET:
#               language_code = self.request.GET.get('language_code')
#               queryset = Tours.objects.language(language_code).order_by('-id')
#           else:
#               queryset = Tours.objects.language().order_by('-id')
#           return queryset


class AbroadLocationAPI(APIView):
     def get(self, request, pk=None):
          try:
             loca = Tour.objects.get(id=pk)
             serializers = LocationSerializer(loca, context={"request": self.request})
             return Response({"data": serializers.data})
          except Exception as e:
              print(e)

          return Response({"status": status.HTTP_404_NOT_FOUND})




class AbroadTicketBuyAPI(GenericAPIView):
    queryset = AbroadTicket.objects.all()
    serializer_class = AbroadTicketSerializer

    def post(self, request, format=None):
        try:
            serializer = self.get_serializer(data=request.data, many=False)
            if serializer.is_valid():
                 serializer.save()
                 return Response({"status":status.HTTP_201_CREATED})
            return Response({"status":status.HTTP_404_NOT_FOUND})

        except Exception as e:
                  print(e)

        return Response({"status": status.HTTP_400_BAD_REQUEST})

