from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields



class TourCategory(models.Model):
     names = models.CharField(max_length=200, verbose_name="Sayohat nomi:")

     def __str__(self):
         return self.names


     class Meta:
          verbose_name =  "Sayohat_turi_"


class TourType(models.Model):
    not_name = models.ManyToManyField(TourCategory, related_name='not_name',  verbose_name="Tour")


    class Meta:
       verbose_name =  "Paket_tur_"






class TagsCategory(models.Model):
     name = models.CharField(max_length=200, verbose_name="Sayohat nomi:")


     def __str__(self):
          return self.name


     class Meta:
          verbose_name =  "Tags_turi_"



class TagsType(models.Model):
    not_name1 = models.ManyToManyField(TagsCategory, related_name='not_name1', verbose_name="Tags")


    class Meta:
       verbose_name =  "Tag_tur_"