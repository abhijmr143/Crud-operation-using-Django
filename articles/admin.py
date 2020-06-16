from django.contrib import admin
from .models import Articles
# Register your models here.


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'updated']


admin.site.register(Articles, ArticlesAdmin)