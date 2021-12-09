from django.shortcuts import redirect, render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Count


from .models import Follower, Profile
from posts.models import ImagePost, TextPost

# View of the profile page
class Home(View):
    template_name = 'profile/profile.html'
    def get(self, request, *args, **kwargs):
        context = {}
        # URL ID handling
        try:
            profile_id = Profile.objects.get(user=request.user).id
        except TypeError:
            return redirect('login')

        if not kwargs.get('profile_id'):
            profile_id = Profile.objects.get(user=request.user).id

        else:
            profile_id = kwargs.get('profile_id')

        # Gets Profiles
        current_profile = Profile.objects.get(id=profile_id)
        context['profile'] = current_profile

        request_user = Profile.objects.get(user=request.user)
        context['request_user'] = request_user

        # Gets posts
        image_posts = ImagePost.objects.all().filter(user=current_profile)
        context['image_posts'] = image_posts
            
        text_posts = TextPost.objects.annotate(total_likes=Count('likes')).filter(user=current_profile)
        context['text_posts'] = text_posts
        



        # Following System
        following_obj = Follower.objects.all()

        request_user_following = following_obj.filter(follower_user_id=request_user, following_user_id=current_profile)
        context['is_following'] = request_user_following

        followers = following_obj.filter(following_user_id=current_profile).count()
        context['followers'] = followers

        following = following_obj.filter(follower_user_id=current_profile).count()
        context['following'] = following


        return render(request, self.template_name, context)
        
        
@method_decorator(login_required(login_url='login'), name='dispatch')
class FollowView(View):
    def get(self, request, *args, **kwargs):
        follower = Profile.objects.get(user=kwargs.get('follower'))
        following = Profile.objects.get(id=kwargs.get('following'))

        if Follower.objects.filter(follower_user_id=follower, following_user_id=following).count() >= 1:
            return redirect('profile', profile_id=kwargs.get('following'))

        if follower == following:
            return redirect('profile', profile_id=kwargs.get('following'))

        follow_model = Follower.objects.create(following_user_id=following,
        follower_user_id=follower)
        follow_model.save()

        return redirect('profile', profile_id=kwargs.get('following'))


@method_decorator(login_required(login_url='login'), name='dispatch')
class UnfollowView(View):
    def get(self, request, *args, **kwargs):
        follower = Profile.objects.get(id=kwargs.get('follower'))
        following = Profile.objects.get(id=kwargs.get('following'))

        if Follower.objects.filter(follower_user_id=follower, following_user_id=following).count() < 1:
            return redirect('profile', profile_id=kwargs.get('following'))

        if follower == following:
            return redirect('profile', profile_id=kwargs.get('following'))

        follow_instance = Follower.objects.get(following_user_id=following, follower_user_id=follower)
        print(follow_instance)
        follow_instance.delete()

        return redirect('profile', profile_id=kwargs.get('following'))

