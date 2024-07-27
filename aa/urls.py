from django.urls import path
from .views import Chatt,Find,DeletRoom



urlpatterns=[
    path('chat/<str:username1>/<str:username2>/',Chatt,name='chat'),
    path('find/<str:username>',Find.as_view(),name='find'),
    path('deleteroom/<str:username>/',DeletRoom.as_view(),name='deleteroom'),
]