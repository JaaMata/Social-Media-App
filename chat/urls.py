from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='chat-home'),
    path('<str:room_name>/', Room.as_view(), name='room'),
]