from django.shortcuts import render
from .models import Category,Image
# Create your views here.
def gallery(request):
    categories=Category.objects.all()
    images=Image.objects.all()
    context={'categories':categories,'images':images}
    return render(request,'main/gallery.html',context)

def viewPhoto(request,pk):
    image=Image.objects.get(id=pk)
    return render(request,'main/photo.html',{'image':image})



def addPhoto(request):
    categories=Category.objects.all()
    context={'categories':categories}
    return render(request,'main/add.html',context)    