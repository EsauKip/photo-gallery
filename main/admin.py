from django.contrib import admin

# Register your models here.
from .models import Image,Category
admin.site.Register(Category)
admin.site.Register(Image)