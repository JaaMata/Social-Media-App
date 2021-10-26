from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    bio = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='profile_images')


class Follower(models.Model):
    following_user_id = models.ForeignKey(Profile, on_delete=CASCADE, related_name="following")
    follower_user_id = models.ForeignKey(Profile, on_delete=CASCADE, related_name="followers")
    created = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    posts = models.OneToOneField(Profile, on_delete=CASCADE)
    image = models.ImageField(upload_to='post_image')
    description = models.CharField(max_length=200)
    date_published = models.DateTimeField(auto_now=True)
