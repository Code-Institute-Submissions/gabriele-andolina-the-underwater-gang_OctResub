from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Defines Post display characteristics in admin panel.
    Provides admin with filter and search post functionality.
    """

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['author', 'title']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Defines Comment display characteristics in admin panel.
    Provides admin with filter, search and approve post functionality.
    """

    list_display = ('name', 'email', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email']
    actions = ['approve_comments']

    def approve_comments(self, queryset):
        """
        Approve comments posted by registered users.
        """
        queryset.update(approved=True)
