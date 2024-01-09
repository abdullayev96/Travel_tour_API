from django.shortcuts import render
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.views import APIView, Response
from rest_framework import status
from  django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Q



class TourAPI(ModelViewSet):
     serializer_class = TravelSerializer

     filter_backends = [DjangoFilterBackend]

     filterset_fields = ['category']


     def get_queryset(self):
         if 'language_code' in self.request.GET:
               language_code = self.request.GET.get('language_code')
               queryset = Tours.objects.language(language_code).order_by('-id')
         else:
               queryset = Tours.objects.language().order_by('id')
         return queryset



class TourFilterAPI(ListAPIView):
     serializer_class = TravelFilterSerializer

     filter_backends = [DjangoFilterBackend]

     filterset_fields = ['category']


     def get_queryset(self):
         if 'language_code' in self.request.GET:
               language_code = self.request.GET.get('language_code')
               queryset = Tours.objects.language(language_code).order_by('-id')
         else:
               queryset = Tours.objects.language().order_by('id')
         return queryset


# class InformationAPI(ModelViewSet):
#      serializer_class = InformationSerializer
#      filter_backends = [DjangoFilterBackend]
#
#      filterset_fields = ['category']
#
#      def get_queryset(self):
#           if 'language_code' in self.request.GET:
#              language_code = self.request.GET.get('language_code')
#              queryset = Tours.objects.language(language_code).order_by('-id')
#           else:
#              queryset = Tours.objects.language().order_by('id')
#           return queryset


class InformationAPI(ListAPIView):
    queryset = Tours.objects.all()
    serializer_class = InformationSerializer

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['category']

    def get_queryset(self):
          if 'language_code' in self.request.GET:
              language_code = self.request.GET.get('language_code')
              queryset = Tours.objects.language(language_code).order_by('-id')
          else:
              queryset = Tours.objects.language().order_by('id')
          return queryset



class TourGalleryAPI(ListAPIView):
     queryset = Tours.objects.all()
     serializer_class = GallerySerializer

     filter_backends = [DjangoFilterBackend]

     filterset_fields = ['category']


     # def get_queryset(self):
     #      if 'language_code' in self.request.GET:
     #          language_code = self.request.GET.get('language_code')
     #          queryset = Tours.objects.language(language_code).order_by('-id')
     #      else:
     #          queryset = Tours.objects.language().order_by('id')
     #      return queryset


# class InformationAPI(ModelViewSet):
#       serializer_class = InformationSerializer
#
#       def get_queryset(self):
#           if 'language_code' in self.request.GET:
#               language_code = self.request.GET.get('language_code')
#               queryset = Tours.objects.language(language_code).order_by('-id')
#           else:
#               queryset = Tours.objects.language().order_by('-id')
#           return queryset
#
#
#       # def get(self, request):
#       #     try:
#       #         infor = Tours.objects.all()
#       #         serializers = InformationSerializer(infor, many=True, context={"request": self.request})
#       #         return Response({"data":serializers.data})
#       #     except Exception as e:
#       #               print(e)
#       #
#       #     return  Response({"status":status.HTTP_404_NOT_FOUND})
#
#


class LocationAPI(ListAPIView):
     queryset = Tours.objects.all()
     serializer_class = LocationSerializer

     filter_backends = [DjangoFilterBackend]

     filterset_fields = ['category']



class TicketBuyAPI(GenericAPIView):
    queryset = TourTicket.objects.all()
    serializer_class = TicketSerializer

    def post(self, request, format=None):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response({"status":status.HTTP_201_CREATED})
            return Response({"status":status.HTTP_404_NOT_FOUND})

        except Exception as e:
                  print(e)

        return Response({"status": status.HTTP_400_BAD_REQUEST})

