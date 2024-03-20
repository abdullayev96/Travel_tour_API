from django.contrib import admin
from .models import *
from parler.admin import TranslatableAdmin


admin.site.register(TourCategory)
admin.site.register(TourType)
admin.site.register(TagsCategory)
admin.site.register(TagsType)

