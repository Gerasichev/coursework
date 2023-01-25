from django.contrib import admin
from gift_cards.models import GiftCard

class GiftCardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'partner_name')
    list_display_links = ('id', )
    search_fields = ('id', 'name', 'partner_name')

admin.site.register(GiftCard, GiftCardsAdmin)
