from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('restaurant/', views.restaurant, name="restaurant" ),
    path('conferencehall/', views.conferencehall, name="conferencehall"),
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/superiortwin/', views.superiortwin, name='superiortwin'),
    path('rooms/standartdeluxe/', views.standartdeluxe, name='standartdeluxe'),
    path('rooms/presidentialsuite/', views.presidentialsuite, name='presidentialsuite'),
    path('rooms/premiersuite/', views.premiersuite, name='premiersuite'),
    path('booking/', views.booking, name="booking")
]