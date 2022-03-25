from email.mime import image
from unicodedata import category
from django.db import models

# Create your models here.
class  Category(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)


    def __str__(self):
        return self.name



class  Image(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(null=False,blank=False)
    description = models.TextField()


    def __str__(self):
        return self.description 