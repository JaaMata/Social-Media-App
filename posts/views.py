from django.shortcuts import render
from django.views import View
from .models import *
from user_profile.models import Follower, Profile

class Home(View):
    template_name = 'posts/home.html'
    def get(self, request, *args, **kwargs):
        context = {}
        request_profile = Profile.objects.get(user=request.user)
        following = Follower.objects.all().filter(follower_user_id=request_profile)
        posts = []
        postsmodel = ImagePost.objects.all()
        
        for i in following:
            posts.append(postsmodel.filter(user=i.following_user_id))
        context['posts'] = posts

        print(posts)

        return render(request, self.template_name, context)

# Create your views here.
