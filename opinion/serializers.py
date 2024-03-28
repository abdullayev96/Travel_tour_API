from rest_framework import serializers
from .models import *
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['images']






# class IncludesTranslationSerializer(serializers.ModelSerializer):
#     class Meta:
#         exclude = ['name']
#
#
#
# class IncludesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Includes
#         translations_serializer = IncludesTranslationSerializer
#         fields = ['name']


class IncludesSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Includes)

    class Meta:
        model = Includes
        fields = ['id','translations']




# class CityTranslationSerializer(serializers.ModelSerializer):
#     class Meta:
#         exclude = ['name']
#
#
#
# class CitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cites
#         translations_serializer = CityTranslationSerializer
#         fields = ['name']


class CitySerializer(TranslatableModelSerializer):

    translations = TranslatedFieldsField(shared_model=Cites)

    class Meta:
        model = Cites
        fields = ['id','translations']





# class HotelTranslationSerializer(serializers.ModelSerializer):
#     class Meta:
#         exclude = ['name']
#
#
#
# class HotelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Hotels
#         translations_serializer = HotelTranslationSerializer
#         fields = ['name']


class  HotelSerializer(TranslatableModelSerializer):

    translations = TranslatedFieldsField(shared_model=Hotels)

    class Meta:
        model = Hotels
        fields = ['id','translations']





class CategoriesTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['name']



class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        translations_serializer = CategoriesTranslationSerializer
        fields = ['name']



class NightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Night
        fields = ['name']




class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour

        fields = ['id','image1','name','day']



class TravelsFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id','image1', 'name']



class DataInformationSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True, read_only=True)
    include = IncludesSerializer(many=True, read_only=True)
    not_include = IncludesSerializer(many=True, read_only=True)
    hotel = HotelSerializer(many=True)
    city = CitySerializer(many=True)
    night = NightSerializer(many=True)
    #category = CategoriesSerializer()


    class Meta:
        model = Tour
        fields = ['id', 'day', 'tour_type', 'people', 'guide', 'image1', 'name', 'body', 'image',
                  'city', 'night','hotel','location', 'include', 'not_include', 'price', 'people_price'
                  ]


class AbroadTicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbroadTicket
        fields = ["full_name",'email', "number", "ticket", "adult",'child',"message","created_at"]
