from django.urls import path, include
from .views import *


urlpatterns = [
    path('/<int:profile_id>', Home.as_view())
]
