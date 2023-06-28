from .models import Review, BoardFeature
from django import forms
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

    class Meta:
        model = BoardFeature
        fields = [
            'board_name',
            'category',
            'manufacturer',
            'special_features',
            'excerpt',
            'featured_image',
        ]
        widgets = {'special_features': SummernoteWidget()}


class ReviewForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Review
        fields = ['body', ]
