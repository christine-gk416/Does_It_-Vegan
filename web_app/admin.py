from django.contrib import admin
from .models import Restaurants
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    allows restaurants to be added in admin pannel
    """
    
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('status', 'updated_on')
    list_display = ('name', 'slug', 'status', 'updated_on')
    search_fields = ['name', 'description']
    summernote_fields = ('description')