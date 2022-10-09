from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Dive


@admin.register(Dive)
class DiveAdmin(SummernoteModelAdmin):
    """
    Defines Dive display characteristics in admin panel.
    """
    list_display = ('diver', 'date', 'title')
    list_filter = ('diver', 'date')
    search_fields = ('diver', 'title')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')
