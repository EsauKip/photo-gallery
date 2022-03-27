from django.test import TestCase
from .models import Category,Location

# Create your tests here.
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.travel= Category(category_name='Travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.travel,Category))
    def test_save_method(self):
        self.travel.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0) 
    def test_delete_category(self):
        self.travel.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)           
class LocationTestCase(TestCase):
    def setUp(self):
        self.location=Location(location_name='Bomet')
        self.location.save_location()
    
    
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))


    def test_save_location(self):
        self.location.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location)>0)

    def test_delete_location(self):
        self.location.delete_location()
        category = Location.objects.all()
        self.assertTrue(len(category) == 0)
    
    
    def test_get_location(self):
        location = Location.get_locations()
        self.assertTrue(location)    