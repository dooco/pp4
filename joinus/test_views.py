from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from unittest import mock
from .models import BoardFeature, Review, Category


class TestDjango(TestCase):

    def test_this_simple_check(self):
        self.assertEqual(1, 1)

    def setUp(self):
        self.category = Category.objects.create(title='Drone', slug='drone')
        self.user = User.objects.create_superuser(username="test", password="test", email="test@test.com")
        self.post = BoardFeature(board_name="Test post", slug="test", author=self.user, category=self.category, manufacturer='test manufacturer', excerpt="Test excerpt", special_features="Test content", featured_image='test image', status=1)
        self.post.save()

    def test_get_post_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_post(self):
        response = self.client.get('board_detail', args=['test'])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'board_detail.html')

    def test_like(self):
        self.client.login(username='test', password='test')
        self.client.post(reverse('board_like', args=['test']))
        post = BoardFeature.objects.filter(slug='test').first()
        self.assertEqual(post.number_of_likes(), 1)

    def test_unlike(self):
        self.client.login(username='test', password='test')
        self.client.post(reverse('board_like', args=['test']))
        self.client.post(reverse('board_like', args=['test']))
        post = BoardFeature.objects.filter(slug='test').first()
        self.assertEqual(post.number_of_likes(), 0)

    def test_comment(self):
        self.client.login(username='test', password='test')
        response = self.client.post(reverse('board_detail', args=['test']), {
            'body': 'This is a test comment'
        })
        self.assertEqual(response.context['commented'], True)

    # def test_can_add_item(self):
    #     response = self.client.post('post_new', {'name': 'Test Added Item'})
    #     self.assertRedirects(response, 'board_detail.html')

    # def test_get_edit_item_page(self):
    #     item = Item.objects.create(name='Test Edit Item')
    #     response = self.client.get(f'/edit/{item.id}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'post_edit.html')

    # def test_can_delete_item(self):
    #     item = Item.objects.create(name='Test Delete Item')
    #     response = self.client.get(f'/delete/{item.id}')
    #     self.assertRedirects(response, '/')
    #     existing_items = Item.objects.filter(id=item.id)
    #     self.assertEqual(len(existing_items), 0)







