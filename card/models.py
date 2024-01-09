from django.db import models
from baseapp.models import BaseModel
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields



class Images(models.Model):
      images = models.ImageField(upload_to="note/")


      class Meta:
          verbose_name = "Rasm_"



class Category(TranslatableModel):
     translations = TranslatedFields(
     name = models.CharField(max_length=200, verbose_name="Kategoriya nomi:"),)

     def __str__(self):
         return self.name


     class Meta:
          verbose_name =  "Kategoriya_"


class City(TranslatableModel):
     translations = TranslatedFields(
     name = models.CharField(max_length=200, verbose_name="Shahar nomi:"),

     )

     def __str__(self):
         return self.name


     class Meta:
          verbose_name =  "Shahar_"



class Hotel(TranslatableModel):
     translations = TranslatedFields(
     name= models.CharField(max_length=200, verbose_name="Mehmonxona"),

      )

     def __str__(self):
               return self.name

     class Meta:
          verbose_name = "Mehmonxona_"



class Tours(TranslatableModel):
    translations = TranslatedFields(
         body = models.TextField(verbose_name="joy haqida malumot:"),)

    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    day = models.CharField(max_length=40, verbose_name="dam olish kunlari:")
    image = models.ManyToManyField(Images, verbose_name="rasmlar", related_name="image")
    image1 = models.ImageField(upload_to="yes/", verbose_name="joy rasmi:")
    price = models.FloatField()
    city = models.ForeignKey(City, related_name='city',on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, related_name='hotel', on_delete=models.CASCADE)
    location = models.URLField(max_length=4000, verbose_name="Lokatsiya::")
    created_at = models.DateField()


    def __str__(self):
          return self.body

    class Meta:
        verbose_name = "Sayohat_"



class TourTicket(models.Model):
     NEW = "Tickets Type 1"
     EXECUTION = "Tickets Type 2"
     COMPLETED = "Tickets Type 3"

     STATUS_CHOICES = (
          (NEW, 'Tickets Type 1'),
          (EXECUTION, 'Tickets Type 2'),
          (COMPLETED, 'Tickets Type 3'),
     )
     one=1
     two=2
     three=3

     STATUS_ADULT = [
               ("Adult", 'Adult'),
               ('one', 1),
               ('two', 2),
               ('three', 3)]

     STATUS_CHILD = [
               ("Child", 'Child'),
               ('one', 1),
               ('two', 2),
               ('three', 3),]


     full_name=models.CharField(max_length=200, verbose_name="To'liq ism, familiyasi:")
     email=models.EmailField(unique=True, verbose_name="Email:")
     number=models.CharField(max_length=40, verbose_name="Raqamizgizni kiriting:")
     ticket=models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="Chipta:", default="Tickets Type 1")
     adults = models.CharField(max_length=20, choices=STATUS_ADULT, verbose_name="Kottalar:", default=1)
     childs = models.CharField(max_length=20, choices=STATUS_CHILD, verbose_name="Bolalar:", default=1)
     message =  models.CharField(max_length=500, verbose_name="Kelgan xabarlar:")
     created_at = models.DateField()

     def __str__(self):
         return self.full_name

     class Meta:
          verbose_name = "Mehmonxona_band_qilish_"



