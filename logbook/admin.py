from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Dive

@admin.register(Dive)
class DiveAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('date', 'location', 'title')
    summernote_fields = ('description')
