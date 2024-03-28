from django.urls import path
from .views import *

from rest_framework.routers import DefaultRouter



urlpatterns =  [

          path('filter/', TourFilterAPI.as_view(), name="filter"),
          path('ticket/', TicketBuyAPI.as_view()),
          path('filter/<int:pk>', InformationDetailAPI.as_view(), name='detail'),


]

router = DefaultRouter()
router.register('', TourAPI, basename='tour')


urlpatterns += router.urls