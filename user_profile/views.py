from django import views
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View


class Home(View):
    def get(request, *args, **kwargs):
        return HttpResponse('asdsad')
