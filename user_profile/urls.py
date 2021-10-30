from django.urls import path, include
from .views import *


urlpatterns = [
    path('', Home.as_view(), name=""),
    path('<int:profile_id>', Home.as_view(), name="profile"),
    path("follow/<int:follower>/<int:following>", FollowView.as_view(), name="follow"),
    path("unfollow/<int:follower>/<int:following>", UnfollowView.as_view(), name="unfollow"),

]
