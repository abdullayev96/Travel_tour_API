from django.urls import path
from .views import *

from rest_framework.routers import DefaultRouter


urlpatterns =  [
          path('gallery/', AbroadGalleryAPI.as_view(), name = "gallery"),
          path('information/<int:pk>/', InformationAPI.as_view(), name = "info"),
          path('location/', AbroadLocationAPI.as_view(), name = "location"),
          path('ticket/', AbroadTicketBuyAPI.as_view(), name = "ticket")

]

router = DefaultRouter()
router.register('tour',AbroadAPI, basename='tour')
#router.register('information/', AbroadInformationAPI, basename='infor')
urlpatterns += router.urls