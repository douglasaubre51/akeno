from django.shortcuts import render

from authentication.models import Worker

# Create your views here.

def get_user_profile_page(request,id):

    user = Worker.objects.get(id=id)

    return render(request,'user_profile.html',{ 'user':user })

