from django.db import models
from parler.models import TranslatableModel, TranslatedFields
#from hvad.models import TranslatableModel, TranslatedFields



class Leader(TranslatableModel):
     translations = TranslatedFields(
          name=models.CharField(max_length=200, verbose_name="To'liq ismi:"),
          job=models.CharField(max_length=200, verbose_name="Mutahasisligi:"))
     image = models.ImageField(upload_to="top/", verbose_name="rasmi:")
     created_at  = models.DateTimeField(auto_now_add=True)


     def __str__(self):
          return self.name


     class Meta:
        verbose_name = "Boshliqlar_"



