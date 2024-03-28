from rest_framework import serializers
from .models import *
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField



class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['images']



class CitySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=City)

    class Meta:
        ref_name = 'Card'
        model = City
        fields = ['id','translations']




# class CityTranslationSerializer(serializers.ModelSerializer):
#     class Meta:
#         exclude = ['name']
#
#
# class CitySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = City
#         translations_serializer = CityTranslationSerializer
#         fields = ['name']



class HotelSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Hotel)

    class Meta:
        ref_name = 'Card'
        model = Hotel
        fields = ['id','translations']


#
# class HotelTranslationSerializer(serializers.ModelSerializer):
#     class Meta:
#         exclude = ['name']
#
#
#
# class HotelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Hotel
#         translations_serializer = HotelTranslationSerializer
#         fields = ['name']



class CategoryTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        translations_serializer = CategoryTranslationSerializer
        fields = ['name']



# class IncludeTranslationSerializer(serializers.ModelSerializer):
#     class Meta:
#         exclude = ['name']
#
#
#
# class IncludeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Include
#         translations_serializer = IncludeTranslationSerializer
#         fields = ['name']
#

class IncludeSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Include)

    class Meta:
        model = Include
        fields = ['id','translations']




class NightSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = 'Card'
        model = Nights
        fields = ['names']


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = 'Card'
        model = Tours
        fields = ['id','image1','name', 'day']



class TravelFilterSerializer(serializers.ModelSerializer):
    #category = CategorySerializer()
    class Meta:
        ref_name = 'Card'
        model = Tours
        fields = ['id','image1', 'name']




class DatasInformationSerializer(serializers.ModelSerializer):
    image = ImagesSerializer(many=True)
    include = IncludeSerializer(many=True)
    not_include = IncludeSerializer(many=True)
    hotel = HotelSerializer(many=True)
    city = CitySerializer(many=True)
    night = NightSerializer(many=True)
    #category = CategorySerializer()


    class Meta:
        model = Tours
        fields = ['id', 'day','tour_type','people','guide','image1','name','body', 'image','city','night','hotel',
                  'location','include','not_include', 'price', 'people_price']



class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourTicket
        fields = ["full_name",'email', "number", "ticket", "adults",'childs',"message","created_at"]
