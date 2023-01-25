from django.contrib import admin
from products.models import Product

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', )
    search_fields = ('id', 'name')

admin.site.register(Product, ProductsAdmin)
