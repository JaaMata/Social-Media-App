from django.urls import re_path

from .consumers import ProfileConsumer

websocket_urlpatterns = [
    re_path('ws/profile/<int:profile_id>', ProfileConsumer.as_asgi())
]