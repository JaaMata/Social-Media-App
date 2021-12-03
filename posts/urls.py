from django.urls import path, include
from .views import *


urlpatterns = [
    path('feed', Home.as_view(), name='feed')

]