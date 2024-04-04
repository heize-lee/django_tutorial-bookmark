from django.contrib import admin
from .models import Bookmark

# Register your models here.
# admin.site.register(Bookmark)

# 데코레이터
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'url')