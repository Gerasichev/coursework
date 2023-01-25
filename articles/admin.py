from django.contrib import admin
from articles.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', )
    search_fields = ('id', 'title')

admin.site.register(Article, ArticleAdmin)
