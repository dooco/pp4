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

    # def test_if_form__receive_data_properly__expect_success(self):
    #     """ Test ProfileEditForm with valid data """
    #     profile = self.__create_valid_user_and_profile()
    #     form_data = {
    #         'board_name': profile.board_name,
    #         'category': profile.category,
    #         'manufacturer': profile.manufacturer,
    #         'special_features': profile.special_features,
    #         'excerpt': profile.excerpt,
    #         'featured_image': profile.featured_image,
    #         }
    #     form = PostForm(data=form_data)
    #     form.instance.user = user
    #     self.assertTrue(form.is_valid())
    #     obj = form.save()
    #     self.assertEqual(obj.first_name, profile.first_name)

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

