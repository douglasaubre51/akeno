from django.shortcuts import render

# Create your views here.

def get_dashboard(request):
    username = request.user.username

    return render(request,'dashboard.html',{ 'username':username })
