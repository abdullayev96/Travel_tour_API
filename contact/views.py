from django.shortcuts import render
from .models import Contact, Link
from .serializers import ContactSerializer, LinkSerializer
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework import status
from rest_framework.views import APIView, Response

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.translation import gettext as _
from rest_framework.viewsets import ModelViewSet
from card.models import TourTicket
from card.serializers import TicketSerializer


class ContactAPI(GenericAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

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


class LinkAPI(APIView):
      def get(self, request):
             try:
                 link = Link.objects.all()
                 serializer = LinkSerializer(link, many=True)
                 return Response({"data":serializer.data})
             except Exception as e:
                       print(e)

             return Response({"status":status.HTTP_404_NOT_FOUND})

