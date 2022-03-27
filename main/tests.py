from django.test import TestCase
from main.models import Category

# Create your tests here.
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.travel= Category(category_name='Travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.travel,Category))   