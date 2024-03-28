from django.contrib import admin
from .models import Contact, Link

from parler.admin import TranslatableAdmin


class ContactAdmin(admin.ModelAdmin):

    list_display = ['name','number', 'message', "created_at"]


    search_fields = ("name",)
    ordering = ("created_at",)


admin.site.register(Contact, ContactAdmin)
admin.site.register(Link)
