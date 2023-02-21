from django.urls import reverse
from django.test import TestCase
from .forms import PostForm, ReviewForm


# class TestPostForm(TestCase):

#     def test_post_name_is_required(self):
#         form = PostForm({'board_name': ''})
#         self.assertFalse(form.is_valid())
#         self.assertIn('board_name', form.errors.keys())
#         self.assertEqual(form.errors['board_name'][0], 'This field is required.')

#     def test_done_field_is_not_required(self):
#         form = PostForm({'board_name': 'Test Board'})
#         self.assertTrue(form.is_valid())

#     def test_fields_are_explicit_in_form_metaclass(self):
#         form = PostForm()
#         self.assertEqual(form.Meta.fields, ['board_name', 'done'])

