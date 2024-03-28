from rest_framework import serializers
from .models import Opinion, DataImage
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField



class DataImageSerializer(TranslatableModelSerializer):

    translations = TranslatedFieldsField(shared_model=DataImage)

    class Meta:
        model = DataImage
        fields = ['translations', 'image', 'image1']




class OpinionSerializer(TranslatableModelSerializer):

    translations = TranslatedFieldsField(shared_model=Opinion)

    class Meta:
        model = Opinion
        fields = ['id','translations', 'image']




