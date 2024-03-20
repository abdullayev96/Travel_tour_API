from django.db import models
from baseapp.models import BaseModel
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields
from location_field.models.plain import PlainLocationField



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



class Include(TranslatableModel):
     translations = TranslatedFields(
     name = models.CharField(max_length=200, verbose_name="Xizmatlar nomi:"),)

     def __str__(self):
         return self.name


     class Meta:
          verbose_name =  "Xizmatlar_"



class Nights(models.Model):
     names = models.CharField(max_length=200, verbose_name="Dam olish soni:")

     def __str__(self):
          return self.names


     class Meta:
          verbose_name = "Kechalar_"



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
         name = models.CharField(max_length=200, verbose_name="Joy nomi:"),
         body = models.TextField(verbose_name="joy haqida malumot:"),
         tour_type= models.TextField(verbose_name=" Paket turi haqida:"),
         people = models.TextField(verbose_name="Odamlar soni:"),
         guide = models.TextField(verbose_name="Ko'rsatuvchilar soni:"))

    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    day = models.CharField(max_length=40, verbose_name="dam olish kunlari:")
    image = models.ManyToManyField(Images, verbose_name="rasmlar", related_name="image")
    image1 = models.ImageField(upload_to="yes/", verbose_name="joy rasmi:")
    price = models.FloatField()
    people_price = models.IntegerField()
    city = models.ManyToManyField(City, related_name='city', verbose_name="Shahar:")
    night = models.ManyToManyField(Nights, related_name='night', verbose_name="Mehmonxonadagi  kechalar:")
    hotel = models.ManyToManyField(Hotel, related_name='hotel', verbose_name="Mehmonxona:")
    include = models.ManyToManyField(Include, verbose_name="o'z ichiga oladi:", related_name="include")
    not_include = models.ManyToManyField(Include, verbose_name="o'z ichiga olmaydi:", related_name="include1")
    location = PlainLocationField(based_fields=['city'], zoom=7)
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



