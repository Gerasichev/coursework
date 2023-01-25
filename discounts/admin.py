from django.contrib import admin
from discounts.models import Discount

class DiscountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', )
    search_fields = ('id', 'title')

admin.site.register(Discount, DiscountsAdmin)
