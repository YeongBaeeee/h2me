from django.contrib import admin
from .models import Diary


@admin.register(Diary)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'tags', 'created_at', 'updated_at']
