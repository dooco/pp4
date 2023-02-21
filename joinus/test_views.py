from django.urls import reverse
from django.test import TestCase
from .models import BoardFeature, Review, Category


class TestDjango(TestCase):

    def test_this_thing_works(self):
        self.assertEqual(1, 1)


# class HomeTests(TestCase):
#     def test_home_view_status_code(self):
#         url = reverse('index')
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'index.html')

    # def test_get_add_item_page(self):
    #     response = self.client.get('/new')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'post_new.html')

    # def test_can_add_item(self):
    #     response = self.client.post('/new', {'name': 'Test Added Item'})
    #     self.assertRedirects(response, '/')

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





    
    # def test_home_url_resolves_home_view(self):
    #     view = resolve('/')
    #     self.assertEquals(view.func, index)



