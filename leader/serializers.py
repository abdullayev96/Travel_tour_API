from rest_framework import serializers
from .models import *
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
#from hvad.contrib.restframework.serializers import TranslationsMixin


# class LeaderSerializer(TranslatableModelSerializer):
#
#     translations = TranslatedFieldsField(shared_model=Leader)
#
#     class Meta:
#         model = Leader
#         fields = ['image','translations']



class LeaderTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['name', 'job']




class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        translations_serializer = LeaderTranslationSerializer
        fields = ['id','image', 'name', 'job']



