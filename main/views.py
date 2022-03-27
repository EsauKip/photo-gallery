
from django.shortcuts import render,redirect
from .models import Category,Image,Location
# Create your views here.
def gallery(request):
    categories=Category.objects.all()
    images=Image.objects.all()
    location=Location.get_locations()
    context={'categories':categories,'images':images,'location':location}
    return render(request,'main/gallery.html',context,)
def image_location(request,location_name):
    location=Location.get_locations()
    image= Image.fetch_by_location(location_name)
    message = f"{location_name}"
    return render(request,'imageLocation.html',{"message":message,"image": image,"location":location})

def viewPhoto(request,pk):
    image=Image.objects.get(id=pk)
    return render(request,'main/photo.html',{'image':image})



def addPhoto(request):
    categories=Category.objects.all()
    if request.method == 'POST':
        data =request.POST
        image=request.FILES.get('image')
        if data['category'] !='none':
            category=Category.objects.get(id=data['category'])
        elif data['category_new']!='':
            category,created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category=None 
            image=Image.objects.create(
            category=category,
            description=data['description'],
            image=image,
        ) 

        return redirect('gallery')       
                  
      

    context={'categories':categories}
    return render(request,'main/add.html',context)    