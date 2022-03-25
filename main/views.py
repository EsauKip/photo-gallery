from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request,'main/gallery.html')

def viewPhoto(request):
    return render(request,'main/photo.html')



def addPhoto(request):
    return render(request,'main/add.html')    