from django.db import models
from baseapp.models import BaseModel
from parler.models import TranslatableModel, TranslatedFields



class Contact(BaseModel):
     name  = models.CharField(max_length=200, verbose_name="Ism Familyasi:")
     number  = models.CharField(max_length=20, verbose_name="Telefon raqami:")
     message = models.TextField(verbose_name="Xabar:")

     def __str__(self):
          return self.name

     class Meta:
        verbose_name = "Kontakt_"



class Link(models.Model):
     number_one = models.CharField(max_length=200, verbose_name="Telefon number 1:")
     number_two = models.CharField(max_length=200, verbose_name="Telefon number 2:")
     email = models.EmailField(unique=True, verbose_name="Email nomi:")
     address = models.CharField(max_length=300, verbose_name="Address nomi:")
     whatsapp  = models.URLField(max_length=4000, verbose_name="whatsapp link:")
     facebook = models.URLField(max_length=4000, verbose_name="Facebook link:")
     telegram = models.URLField(max_length=4000, verbose_name="Telegram  link:")
     youtobe = models.URLField(max_length=4000, verbose_name="You tobe  link:")
     instagram = models.URLField(max_length=4000, verbose_name="Instagram  link:")


     def __str__(self):
          return self.number_one


     class Meta:
          verbose_name = "Link_nomlar_"





