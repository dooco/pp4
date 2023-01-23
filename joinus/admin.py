from django.contrib import admin
from .models import Board_feature
from .models import Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Board_feature)
class Board_featureAdmin(SummernoteModelAdmin):
    list_display = ('board_name', 'slug', 'status', 'created_on')
    search_fields = ['manufacturer', 'special_features']
    prepopulated_fields = {'slug': ('board_name',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('special_features', 'excerpt',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'board', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_review']

#     def approve_review(self, request, queryset):
#         queryset.updata(approved=True)
