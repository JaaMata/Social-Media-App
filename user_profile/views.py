from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View

from .models import Follower, Post, Profile

# View of the profile page
class Home(View):
    template_name = 'profile/profile.html'
    def get(self, request, *args, **kwargs):
        context = {}
        # Get the profile and the post related to them
        
        if kwargs.get('id'):
            id = kwargs.get('id')
        else:
            id = request.user.id


        profiles = Profile.objects.all()
        profile = profiles.filter(id=id).first()
        context['profile'] = profile
        posts = Post.objects.all().filter(user=profile)
        context['posts'] = posts

        # Follower and Following Count
        follow_model = Follower.objects.all()
        followers = follow_model.filter(following_user_id=profile).count()
        following = follow_model.filter(follower_user_id=profile).count()
        context['followers'] = followers
        context['following'] = following

        # Follow logic
        request_user_profile = profiles.filter(user=request.user)[0]
        follower_query = Follower.objects.all().filter(follower_user_id=request_user_profile)
        if follower_query:
            context['followed'] = True
        
        context['current_profile_id'] = profile.id
        context['request_profile_id'] = request_user_profile.id

        return render(request, self.template_name, context)


class FollowView(View):
    def get(self, request, *args, **kwargs):
        follower = Profile.objects.get(id=kwargs.get('follower'))
        following = Profile.objects.get(id=kwargs.get('following'))

        if follower == following:
            return redirect('profile', profile_id=kwargs.get('following'))

        follow_model = Follower.objects.create(following_user_id=following,
        follower_user_id=follower)
        follow_model.save()

        return redirect('profile', profile_id=kwargs.get('following'))


class UnfollowView(View):
    def get(self, request, *args, **kwargs):
        follower = Profile.objects.get(id=kwargs.get('follower'))
        following = Profile.objects.get(id=kwargs.get('following'))

        if follower == following:
            return redirect('profile', profile_id=kwargs.get('following'))

        follow_instance = Follower.objects.get(following_user_id=following,follower_user_id=follower)
        follow_instance.delete()

        return redirect('profile', profile_id=kwargs.get('following'))
