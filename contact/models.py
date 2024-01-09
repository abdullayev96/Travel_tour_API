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





