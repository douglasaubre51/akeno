from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse

from .forms import SignupForm

# Create your views here.

def get_signup_page(request):

    if request.method == 'GET':

        form = SignupForm()
        context = {
                'form':form
                }
        template = loader.get_template('registration/signup.html')

        return HttpResponse(template.render(context,request))

