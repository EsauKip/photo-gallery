from email.mime import image
from unicodedata import category
from django.db import models

# Create your models here.
class  Category(models.Model):
    category_name = models.CharField(max_length=100,null=False,blank=False)


    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()    



class  Image(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(null=False,blank=False)
    description = models.TextField()


    def __str__(self):
        return self.description 

class Location(models.Model):
    
    name=models.CharField(null=False,blank=False,max_length=100)


    
    def __str__(self):
        return self.name 
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def get_locations(cls):
        location=Location.objects.all()

        return location    