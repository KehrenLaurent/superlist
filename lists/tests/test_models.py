from django.test import TestCase
from lists.models import Item, List

# Create your tests here.


class ListAndItemModelsTest(TestCase):
    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the seconde'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(list_, saved_list)

        saved_items = Item.objects.all()
        self.assertEqual(2, saved_items.count())

        first_saved_item = saved_items[0]
        seconde_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(seconde_saved_item.text, 'Item the seconde')
        self.assertEqual(seconde_saved_item.list, list_)
