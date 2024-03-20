from django.contrib import admin
from .models import *

from parler.admin import TranslatableAdmin

#
# class ToursTicketAdmin(admin.ModelAdmin):
#
#     list_display = ["full_name",'email', "number", "ticket", "adult",'child',"message","created_at"]
#
#
#     #list_filter = ('name','number' )
#     search_fields = ("name", "city", "day")
#
#

admin.site.register(TourTicket)
admin.site.register(Category, TranslatableAdmin)
admin.site.register(Nights)
admin.site.register(Include, TranslatableAdmin)
admin.site.register(Hotel, TranslatableAdmin)
admin.site.register(City, TranslatableAdmin)
admin.site.register(Tours, TranslatableAdmin)
admin.site.register(Images)

