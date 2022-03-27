from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/',views.viewPhoto,name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('location/<str:location_name>/',views.image_location,name ='location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)