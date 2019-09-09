from django.test import TestCase
from rest_framework.test import APITestCase
from restapp.models import Menu

# Create your tests here.


class MenuCreateTestCase(APITestCase):
    def test_create_product(self):
        initial_menu_count = Menu.objects.count()
        menu_attrs = {
            'name': 'New Menu',
            'description': 'Cool Menu',
            'price': '128.99',
            'course': 'Main',
        }
        response = self.client.post('api/v1/menu/new', menu_attrs)
        # if response.status_code != 201:
        #     print(response)
        # self.assertEqual(
        #     Menu.objects.count(),
        #     initial_menu_count + 1,
        # )

# class MenuDestroyTestCase(APITestCase):
#     def test_delete_menu(self):
