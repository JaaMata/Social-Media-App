from django.urls import re_path, path

from chat.consumers import ChatConsumer
from user_profile.consumers import ProfileConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
    path('ws/profile/<int:profile_id>', ProfileConsumer.as_asgi()),

]