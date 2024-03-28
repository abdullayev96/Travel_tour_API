from django.urls import path
from .views import *


urlpatterns = [
          path('', OpinionAPI.as_view()),
          path('data/', DataImageAPI.as_view())

]