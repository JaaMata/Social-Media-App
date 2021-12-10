from django.shortcuts import render
from django.views import View
from .models import *
from user_profile.models import Follower, Profile
from django.db.models import Count



class Home(View):
    template_name = 'posts/home.html'
    def get(self, request, *args, **kwargs):
        context = {}
        request_profile = Profile.objects.get(user=request.user)
        following = Follower.objects.all().filter(follower_user_id=request_profile.id)
        postsmodel = ImagePost.objects.annotate(likees=Count('likes'))


        posts = postsmodel.filter(user=[i.following_user_id for i in following][0]) 
        context['posts'] = posts

        return render(request, self.template_name, context)

# Create your views here.
