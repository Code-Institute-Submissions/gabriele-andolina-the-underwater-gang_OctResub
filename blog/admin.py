from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['author', 'title']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email']
