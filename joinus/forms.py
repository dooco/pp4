from .models import Review, BoardFeature
from django import forms


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

    class Meta:
        model = BoardFeature
        fields = ['board_name', 'category', 'manufacturer', 'special_features', 'excerpt', 'featured_image',]
        # featured_image = forms.ImageField(label='Featured Image', required=True,)


class ReviewForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(PostCreate, self).__init__(*args, **kwargs)

    class Meta:
        model = Review
        fields = ['body', ]
