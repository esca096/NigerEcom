from django.contrib import admin
from blog.models import Article
# Register your models here.

class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    
admin.site.register(Article, AdminArticle)