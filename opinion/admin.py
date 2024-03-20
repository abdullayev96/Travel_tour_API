from django.contrib import admin
from .models import *


from parler.admin import TranslatableAdmin


class TourAdmin(admin.ModelAdmin):

    list_display = ["full_name",'email', "number", "ticket", "adult",'child',"message","created_at"]



    list_filter = ('full_name',)
    search_fields = ("full_name", "email", "ticket")



admin.site.register(AbroadTicket, TourAdmin)
admin.site.register(Categories, TranslatableAdmin)
admin.site.register(Night)
admin.site.register(Images)
admin.site.register(Includes, TranslatableAdmin)
admin.site.register(Tour, TranslatableAdmin)
admin.site.register(Hotels, TranslatableAdmin)
admin.site.register(Cites, TranslatableAdmin)

