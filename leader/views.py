from django.shortcuts import render
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.views import APIView, Response
from rest_framework.viewsets import ModelViewSet


class LeaderAPI(ModelViewSet):
    serializer_class = LeaderSerializer



    def get_queryset(self):
        if 'language_code' in self.request.GET:
            language_code = self.request.GET.get('language_code')
            queryset = Leader.objects.language(language_code).order_by('-id')
        else:
            queryset = Leader.objects.language().order_by('id')
        return queryset









