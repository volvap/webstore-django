from django.test import TestCase
from .models import Item
from django.test import Client


class ItemTestCase(TestCase):
    def item_test(self):
        item = Item()
        item.title = "New title"
        item.price = 12.3
        item.basic_info = "asd"
        item.save()

        record = Item.objects.get(pk=1)
        self.assertEqual(record, item)


    def test_response(self):
        self.client = Client()
        response = self.client.get('/main')
        self.assertEqual(response.status_code, 200)
