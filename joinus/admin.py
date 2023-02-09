from django.contrib import admin
from django.contrib.auth.models import User
from .models import BoardFeature, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BoardFeature)
class BoardFeatureAdmin(SummernoteModelAdmin):
    list_display = ('board_name', 'slug', 'status', 'created_on')
    search_fields = ['manufacturer', 'special_features']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('board_name',)}

    # summernote_fields = ('special_features', 'excerpt',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'board', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['user', 'body']
    actions = ['approve_review']

    def approve_review(self, request, queryset):
        queryset.update(approved=True)
