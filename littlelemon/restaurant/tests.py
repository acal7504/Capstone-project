from django.test import TestCase
from . models import Menu

# Create your tests here.
def MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Icecream',price='80',inventory='100')
        self.assertEqual(item, "IceCream : 80")
