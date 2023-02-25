from django.urls import reverse
from django.test import TestCase
from .forms import ReviewForm, PostForm


class TestReviewForm(TestCase):
    
    def test_body_is_required(self):
        form = ReviewForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')


class TestPostForm(TestCase):
    def test_body_is_required(self):
        form = PostForm({'board_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('board_name', form.errors.keys())
        self.assertEqual(form.errors['board_name'][0], 'This field is required.')