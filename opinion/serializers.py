from rest_framework import serializers
from .models import *
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField




class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['images']



class CitesSerializer(TranslatableModelSerializer):

    translations = TranslatedFieldsField(shared_model=Cites)

    class Meta:
        model = Cites
        fields = ['translations']


class HotelsSerializer(TranslatableModelSerializer):

    translations = TranslatedFieldsField(shared_model=Hotels)

    class Meta:
        model = Hotels
        fields = ['translations']



class InformationSerializer(TranslatableModelSerializer):
    city = CitesSerializer()
    hotel = HotelsSerializer()

    class Meta:
        model = Tour
        fields = ['id', 'city','day','hotel']





class CityTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['name']



class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cites
        translations_serializer = CityTranslationSerializer
        fields = ['name']




class HotelTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['name']



class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        translations_serializer = HotelTranslationSerializer
        fields = ['name']



class TravelTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['name']



class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        translations_serializer = TravelTranslationSerializer
        fields = ['id','image1', 'name', 'day', 'price']



class GallerySerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = ['id', 'image']



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id','location']



class AbroadTicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbroadTicket
        fields = ["full_name",'email', "number", "ticket", "adult",'child',"message","created_at"]
