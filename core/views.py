from django.shortcuts import render
from django.views import View
# Create your views here.

class WelcomeView(View):
    template_name = 'core/welcome.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
