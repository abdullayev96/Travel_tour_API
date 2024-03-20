from django.shortcuts import render
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView
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
         if 'lang' in self.request.GET:
               language_code = self.request.GET.get('lang')
               queryset = Tours.objects.language(language_code).order_by('-id')
         else:
               queryset = Tours.objects.language().order_by('id')
         return queryset



class TourFilterAPI(ListAPIView):
     serializer_class = TravelFilterSerializer

     filter_backends = [DjangoFilterBackend]

     filterset_fields = ['category']


     def get_queryset(self):
         if 'lang' in self.request.GET:
               language_code = self.request.GET.get('lang')
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


class InformationDetailAPI(RetrieveAPIView):
    queryset = Tours.objects.all()
    serializer_class = DatasInformationSerializer

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['category']

    def get_queryset(self):
          if 'lang' in self.request.GET:
              language_code = self.request.GET.get('lang')
              queryset = Tours.objects.language(language_code).order_by('-id')
          else:
              queryset = Tours.objects.language().order_by('id')
          return queryset


#
# class InformationDetailAPI(APIView):
#
#     def get(self, request, pk=None):
#           try:
#               info = Tours.objects.get(id=pk)
#               serializers = DatasInformationSerializer(info, context={"request":self.request})
#               return Response({"data":serializers.data})
#
#           except Exception as e:
#                     print(e)
#
#           return Response({"status":status.HTTP_404_NOT_FOUND})
#

#
# class TicketBuyAPI(GenericAPIView):
#     queryset = TourTicket.objects.all()
#     serializer_class = TicketSerializer
#
#     def post(self, request, format=None):
#         try:
#             serializer = self.get_serializer(data=request.data)
#             if serializer.is_valid():
#                  serializer.save()
#                  print(serializer.data)
#                  return Response({"status":status.HTTP_201_CREATED})
#             return Response({"status":status.HTTP_404_NOT_FOUND})
#
#         except Exception as e:
#                   print(e)
#
#         return Response({"status": status.HTTP_400_BAD_REQUEST})


class TicketBuyAPI(APIView):
    def post(self, request, format=None):
        data=request.data
        try:
            serializer = TicketSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                 serializer.save()
                 print(serializer.data)
                 return Response({"status":status.HTTP_201_CREATED})
            return Response({"status":status.HTTP_404_NOT_FOUND})

        except Exception as e:
                  print(e)

        return Response({"status": status.HTTP_400_BAD_REQUEST})
