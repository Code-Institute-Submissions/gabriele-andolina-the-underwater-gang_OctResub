from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['author', 'title']
    summernote_fields = ('content')
