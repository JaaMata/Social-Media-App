from django.db import models
from user_profile.models import Profile
from django.db.models.deletion import CASCADE

# Create your models here.



class LikeModel(models.Model):
    user = models.ForeignKey(Profile, on_delete=CASCADE)


class ImagePost(models.Model):
    image = models.ImageField(upload_to='post_image')
    description = models.CharField(max_length=200)
    date_published = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Profile, on_delete=CASCADE, null=True)
    likes = models.ManyToManyField(LikeModel, blank=True)


    def __str__(self) -> str:
        return f"{self.user.user.username}'s Image Post"


class TextPost(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(Profile, on_delete=CASCADE)
    date_published = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(LikeModel, blank=True)


    def __str__(self) -> str:
        return f"{self.user.user.username}'s Text Post"

