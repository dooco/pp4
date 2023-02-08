from django.contrib import admin
from django.contrib.auth.models import User
from .models import Board_feature, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Board_feature)
class Board_featureAdmin(SummernoteModelAdmin):
    list_display = ('board_name', 'slug', 'status', 'created_on')
    search_fields = ['manufacturer', 'special_features']
    prepopulated_fields = {'slug': ('board_name',)}
    list_filter = ('status', 'created_on')
    # summernote_fields = ('special_features', 'excerpt',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'board', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['user', 'body']
    actions = ['approve_review']

    def approve_review(self, request, queryset):
        queryset.update(approved=True)
