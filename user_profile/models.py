from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    bio = models.CharField(max_length=80, null=True)
    profile_image = models.ImageField(upload_to='profile_images', default='profile_images/default.svg')

    def __str__(self) -> str:
        return self.user.username


class Follower(models.Model):
    following_user_id = models.ForeignKey(Profile, on_delete=CASCADE, related_name="following")
    follower_user_id = models.ForeignKey(Profile, on_delete=CASCADE, related_name="followers")
    created = models.DateTimeField(auto_now_add=True)


