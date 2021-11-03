from django.shortcuts import redirect, render
from django.views import View
from .forms import *

from user_profile.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class Signup(View):
    template_name = 'authentication/signup.html'
    form_class = SignupForm()
    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        context = {}
        form = SignupForm(request.POST)
        context['form'] = form
        if form.is_valid():
            password = form['password1'].value()
            username = form['username'].value()
            email = form['email'].value()
            first_name = form['first_name'].value()
            last_name = form['last_name'].value()

            user = User(
                email=email,
                password=password,
                username=username,
                first_name=first_name,
                last_name=last_name)
            user.save()
            profile = Profile(user=user)
            profile.save()
            login(request, user)
            print(request.user.username)
            return redirect('profile', profile_id=1)
        return render(request,self.template_name, context)
        
class LoginView(View):
    template_name = 'authentication/login.html'
    form_class = LoginForm
    
    def get(self,request, *args, **kwargs):
        context = {'form': self.form_class}
        return render(request, self.template_name, context)

    def post(self,request, *args, **kwargs):
        context = {}
        form = LoginForm(request.POST)
        context['form'] = form

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            print('saasf')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('profile', profile_id=1)
        return render(request, self.template_name, context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')