from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price']
    list_editable = ['description', 'price']
    list_filter = ['name', ]


admin.site.register(Item, ItemAdmin)
