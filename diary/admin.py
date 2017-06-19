from django.contrib import admin
from .models import Diary, Comment, Tag


@admin.register(Diary)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'created_at', 'updated_at']
    actions = ['make_Public', 'make_Secret']


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('tag_set')


    def tag_list(request, post):
        return ', '.join(tag.name for tag in Diary.tag_set.all())  # list comprehension 문법

    def make_Public(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{} sucessfully marked as Public'.format(updated_count))

    def make_Secret(self, request, queryset):
        updated_count = queryset.update(status='s')
        self.message_user(request, '{} sucessfully marked as Secret'.format(updated_count))

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author']
    #list_select_related = ['post']


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('diary')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass