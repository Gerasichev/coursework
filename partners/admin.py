from django.contrib import admin
from partners.models import Partner

class PartnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', )
    search_fields = ('id', 'name')

admin.site.register(Partner, PartnersAdmin)