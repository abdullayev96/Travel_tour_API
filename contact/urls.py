from django.urls import path
from .views import ContactAPI, LinkAPI


urlpatterns = [
          path("", ContactAPI.as_view()),
          path("link", LinkAPI.as_view()),



]