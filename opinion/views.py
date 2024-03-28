from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView

from  django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters




class AbroadAPI(ModelViewSet):
     serializer_class = TravelSerializer


     def get_queryset(self):
         if 'lang' in self.request.GET:
               language_code = self.request.GET.get('lang')
               queryset = Tour.objects.language(language_code).order_by('-id')
         else:
               queryset = Tour.objects.language().order_by('id')
         return queryset



class AbroadFilterAPI(ListAPIView):
     serializer_class = TravelsFilterSerializer

     filter_backends = [DjangoFilterBackend]

     filterset_fields = ['category']

     def get_queryset(self):
         if 'lang' in self.request.GET:
               language_code = self.request.GET.get('lang')
               queryset = Tour.objects.language(language_code).order_by('-id')
         else:
               queryset = Tour.objects.language().order_by('id')
         return queryset



class TourInformationDetailAPI(RetrieveAPIView):
     serializer_class = DataInformationSerializer

     filter_backends = [DjangoFilterBackend]

     filterset_fields = ['category']


     def get_queryset(self):
         if 'lang' in self.request.GET:
               language_code = self.request.GET.get('lang')
               queryset = Tour.objects.language(language_code).order_by('-id')
         else:
               queryset = Tour.objects.language().order_by('id')
         return queryset



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

