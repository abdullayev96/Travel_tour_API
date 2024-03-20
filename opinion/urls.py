from django.urls import path
from .views import *

from rest_framework.routers import DefaultRouter


urlpatterns =  [

          path('ticket/', AbroadTicketBuyAPI.as_view(), name = "ticket"),
          path('filter/',AbroadFilterAPI.as_view(), name = "filter"),
          path('filter/<int:pk>',TourInformationDetailAPI.as_view(), name = "data"),

]


router = DefaultRouter()
router.register('tour',AbroadAPI, basename='tour')

urlpatterns += router.urls