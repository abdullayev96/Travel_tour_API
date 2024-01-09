from django.urls import path
from .views import ContactAPI


urlpatterns = [
          path("", ContactAPI.as_view()),


]