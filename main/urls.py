from django.urls import path

from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/',views.viewPhoto,name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('location/<str:location_name>/',views.image_location,name ='location'),
]