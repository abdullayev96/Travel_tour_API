from django.urls import path
from .views import *


urlpatterns = [
    path('', TypeAPI.as_view()),
    path('tags/', TagsTypeAPI.as_view())

]