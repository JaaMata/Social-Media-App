from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='chat-home'),
    path('<str:room_name>/', room, name='room'),
]