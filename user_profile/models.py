from django.db import models
from django.auth.models import User

class Post(models.Model):
    posts = models.OneToOneField(Profile)
    image = models.ImageField()
    description = models.CharField(max_length=200)
    date_published = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASECADE)
    bio = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='profile_images')

