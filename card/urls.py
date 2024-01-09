from django.urls import path
from .views import *

from rest_framework.routers import DefaultRouter

urlpatterns =  [
          path('gallery/', TourGalleryAPI.as_view(), name = "gallery"),
          path('information/', InformationAPI.as_view(), name = "infor"),
          path('location/', LocationAPI.as_view(), name = "location"),
          path('ticket/', TicketBuyAPI.as_view(), name = "ticket"),
          path('filter/',TourFilterAPI.as_view(), name = "filter"),


]

router = DefaultRouter()
router.register('', TourAPI, basename='tour')
#router.register('filter', TourFilterAPI, basename='filter')

urlpatterns += router.urls