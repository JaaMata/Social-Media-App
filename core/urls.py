from django.urls import path, include
from .views import *

urlpatterns = [
    path('', WelcomeView.as_view(), name="welcome"),

]
