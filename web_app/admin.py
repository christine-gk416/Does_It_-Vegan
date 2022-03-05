from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Restaurant, Review


# code based of codeinstitue blog project
@admin.register(Restaurant)
class PostAdmin(SummernoteModelAdmin):
    """
    allows restaurants to be added and managed in admin pannel
    """

    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('status', 'updated_on')
    list_display = ('name', 'slug', 'status', 'updated_on')
    search_fields = ['name', 'description']
    summernote_fields = ('description')


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """
    allows reviews to be added and managed in admin pannel
    """

    list_filter = ('approved', 'created_on')
    list_display = ('title', 'approved', 'created_on')
    search_fields = ['title', 'body', 'restaurant']
    summernote_fields = ('body')
