from rest_framework import serializers
from .models import *
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['images']




class CitiesSerializer(TranslatableModelSerializer):

    translations = TranslatedFieldsField(shared_model=City)

    class Meta:
        model = City
        fields = ['translations']


class HotelsSerializer(TranslatableModelSerializer):

    translations = TranslatedFieldsField(shared_model=Hotel)

    class Meta:
        model = Hotel
        fields = ['translations']



class InformationSerializer(TranslatableModelSerializer):
    city = CitiesSerializer()
    hotel = HotelsSerializer()

    class Meta:
        model = Tours
        fields = ['id', 'city','day','hotel']




class CityTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        translations_serializer = CityTranslationSerializer
        fields = ['name']


# class HotelSerializer(TranslatableModelSerializer):
#
#     translations = TranslatedFieldsField(shared_model=Hotel)
#
#     class Meta:
#         model = Hotel
#         fields = ['translations']


class HotelTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['name']



class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        translations_serializer = HotelTranslationSerializer
        fields = ['name']


class CategoryTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['name']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        translations_serializer = CategoryTranslationSerializer
        fields = ['name']






class TravelSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Tours
        fields = ['id','image1', 'category', 'day', 'price']



class TravelFilterSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Tours
        fields = ['id','image1', 'category']



class TravelInformationSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    hotel = HotelSerializer()
    class Meta:
        model = Tours
        fields = ['id', 'city', 'day', 'hotel']


class GallerySerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Tours
        fields = ['id','image']



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = ['id','location']



class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourTicket
        fields = ["full_name",'email', "number", "ticket", "adults",'childs',"message","created_at"]
