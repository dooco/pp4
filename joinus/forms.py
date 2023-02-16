from .models import Review, BoardFeature
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = BoardFeature
        fields = ['board_name', 'category', 'manufacturer', 'special_features', 'excerpt', 'featured_image',
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['body',]
