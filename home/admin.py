from django.contrib import admin

from parler.admin import TranslatableAdmin
from .models import *



admin.site.register(DataImage, TranslatableAdmin)
admin.site.register(Opinion, TranslatableAdmin)
