from django.contrib import admin
from authentication.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'nickname')
    list_display_links = ('id', )
    search_fields = ('nickname', 'email')

admin.site.register(User, UserAdmin)
