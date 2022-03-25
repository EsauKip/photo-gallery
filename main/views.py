from django.shortcuts import render
from .models import Category,Image
# Create your views here.
def gallery(request):
    categories=Category.objects.all()
    context={'categories':categories}
    return render(request,'main/gallery.html',context)

def viewPhoto(request):
    return render(request,'main/photo.html')



def addPhoto(request):
    return render(request,'main/add.html')    