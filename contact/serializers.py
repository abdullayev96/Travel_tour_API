from rest_framework import serializers
#import hvad.contrib.restframework.HyperlinkedTranslatableModelSerializer
from .models import Contact, Link
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField


#
# class ContactSerializer(TranslatableModelSerializer):
#
#     translations = TranslatedFieldsField(shared_model=Contact)
#
#     class Meta:
#         model = Contact
#         fields = ['translations']




# class ContactTranslationSerializer(serializers.ModelSerializer):
#     class Meta:
#         exclude = ['name', 'number', 'message']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'number', 'message']



class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"

