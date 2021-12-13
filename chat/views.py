from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
@method_decorator(login_required(login_url='login'), name='dispatch')
class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chat/index.html')




def room(request, room_name):
    return render(request, 'chat/room.html',context={
        'room_name':room_name
    })