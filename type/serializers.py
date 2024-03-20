from .models import *
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from rest_framework import serializers


class CategoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourCategory
        fields = ['names']



class TourTypeSerializer(serializers.ModelSerializer):
    not_name = CategoryTypeSerializer(many=True)
    class Meta:
        model = TourType
        fields = ['not_name']





class CategoryTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsCategory
        fields = ['name']



class TagsTypeSerializer(serializers.ModelSerializer):
    not_name1 = CategoryTagsSerializer(many=True)
    class Meta:
        model = TagsType
        fields = ['not_name1']