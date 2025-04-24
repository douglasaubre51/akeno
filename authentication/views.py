from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse

from . models import Account

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

    elif request.method == 'POST':

        form = SignupForm(request.POST)

        if form.is_valid():

            form.save()

            username = form.cleaned_data['username']
            print(username)
            password = form.cleaned_data['password']
            print(password)

            account = Account.objects.get(username=username)
            account.set_password(password)
            account.save()

            return redirect('/')

        else:

            return render(request,'registration/signup.html',{ 'form':form })
