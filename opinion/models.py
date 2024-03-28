from django.db import models
from baseapp.models import BaseModel
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields

# from django.contrib.gis.geos import Point
# from django.contrib.gis.db.models.functions import Distance
from location_field.models.plain import PlainLocationField

# class Place(models.Model):
#     city = models.CharField(max_length=255)
#     location = PlainLocationField(based_fields=['city'], zoom=7)


class Images(models.Model):
      images = models.ImageField(upload_to="note/")


      class Meta:
          verbose_name = "Rasm_"


class Categories(TranslatableModel):
     translations = TranslatedFields(
     name = models.CharField(max_length=200, verbose_name="Kategoriya nomi:"),)

     def __str__(self):
         return self.name


     class Meta:
          verbose_name =  "Kategoriya_"



class Includes(TranslatableModel):
     translations = TranslatedFields(
     name = models.CharField(max_length=200, verbose_name="Xizmatlar nomi:"),)

     def __str__(self):
         return self.name


     class Meta:
          verbose_name =  "Xizmatlar_"



class Night(models.Model):
     name = models.CharField(max_length=200, verbose_name="Mehmonxonada qolishlar soni:")

     def __str__(self):
          return self.name


     class Meta:
          verbose_name = "Kechalar_"



class Cites(TranslatableModel):
     translations = TranslatedFields(
     name = models.CharField(max_length=200, verbose_name="Shahar nomi:"),

     )

     def __str__(self):
         return self.name


     class Meta:
          verbose_name =  "Shahar_"



class Hotels(TranslatableModel):
     translations = TranslatedFields(
     name= models.CharField(max_length=200, verbose_name="Mehmonxona"),

      )

     def __str__(self):
          return self.name

     class Meta:
          verbose_name = "Mehmonxona_"



class Tour(TranslatableModel):
    translations = TranslatedFields(
         name=models.CharField(max_length=200, verbose_name="Joy nomi:"),
         body = models.TextField(verbose_name="joy haqida malumot:"),
         tour_type=models.TextField(verbose_name=" Paket turi haqida:"),
         people=models.TextField(verbose_name="Odamlar soni:"),
         guide=models.TextField(verbose_name="Ko'rsatuvchilar soni:"),)


    day = models.CharField(max_length=40, verbose_name="dam olish kunlari:")
    image = models.ManyToManyField(Images, verbose_name="rasmlar", related_name="image")
    image1 = models.ImageField(upload_to="yes/", verbose_name="joy rasmi:")
    price = models.FloatField()
    people_price = models.IntegerField()
    city = models.ManyToManyField(Cites, related_name='city', verbose_name="Shahar:")
    hotel = models.ManyToManyField(Hotels, related_name='hotel', verbose_name="Mehmonxona")
    night = models.ManyToManyField(Night, related_name='night', verbose_name="Mehmonxonadagi  kechalar:")
    category = models.ForeignKey(Categories, related_name='category', on_delete=models.CASCADE)
    include = models.ManyToManyField(Includes, verbose_name="o'z ichiga oladi:", related_name="include")
    not_include = models.ManyToManyField(Includes, verbose_name="o'z ichiga olmaydi:", related_name="include1")
    location = PlainLocationField(based_fields=['city'], zoom=7)
    created_at = models.DateField()


    def __str__(self):
          return self.body

    class Meta:
        verbose_name = "Sayohat_"



class AbroadTicket(models.Model):
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
     adult = models.CharField(max_length=20, choices=STATUS_ADULT, verbose_name="Kottalar:", default=1)
     child = models.CharField(max_length=20, choices=STATUS_CHILD, verbose_name="Bolalar:", default=1)
     message=  models.CharField(max_length=500, verbose_name="Kelgan xabarlar:")
     created_at = models.DateField()

     def __str__(self):
         return self.full_name

     class Meta:
          verbose_name = "hotel_buyurtma_qilish_"


