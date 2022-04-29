from django.test import TestCase
from django.test import Client
from .models import Restaurant, Dish
from django.contrib.auth.models import User
# Create your tests here.

class TestViews(TestCase):
    """
    test for views will be defined in this class
    """
    
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods

        User.objects.create_user(
            username='testUser',
            password="testPassword"
        )

        Restaurant.objects.create(
            name='Test Name',
            description='Test Description',
            adress='Test Adress',
            townCity='Test Town',
            added_by=User.objects.get(id=1)
        )

        Dish.objects.create(
            name='Test Dish Name',
            price='12',
            description='Test Dish Description',
            restaurant=Restaurant.objects.get(id=1),
            type='Main'
        )

    def test_index(self):
        """
        test if the indext.html page returns a 200 status code
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_sign_up(self):
        """
        test if the sign_up.html page returns a 200 status code
        """
        response = self.client.get('/sign_up/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')

    def test_restaurant_detail(self):
        """
        test if the restaurant_detail.html page returns a 200 status code
        """
        response = self.client.get('/restaurant_detail/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_detail.html')

    def test_search_results(self):
        """
        test if the serch_results.html page returns a 200 status code
        """
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_results.html')

