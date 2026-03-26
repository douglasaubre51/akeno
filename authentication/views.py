from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse

from . models import Account,Worker

from .forms import SignupForm,WorkerSignupForm

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
        # req.FILES is for image upload
        form = SignupForm(request.POST,request.FILES)

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


def get_worker_signup_page(request):
    if request.method == 'GET':
        form = WorkerSignupForm()
        context = {
                'form':form
                }
        template = loader.get_template('registration/worker-signup.html')

        return HttpResponse(template.render(context,request))

    elif request.method == 'POST':
        form = WorkerSignupForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            print(username)
            password = form.cleaned_data['password']
            print(password)

            account = Worker.objects.get(username=username)
            account.set_password(password)
            account.save()

            return redirect('/')

        else:
            return render(request,'registration/worker-signup.html',{ 'form':form })
