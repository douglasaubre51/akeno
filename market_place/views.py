import datetime
from django.http import HttpResponse
from django.shortcuts import render

from authentication.models import Account,Worker

# Create your views here.

def get_current_time(request):

    current_time = datetime.datetime.now()

    html_string = '<html><body><h1>tik tok : %s</h1></body></html>' % current_time

    return HttpResponse(html_string)


def get_worker_market_place(request):

    worker_model = Worker.objects.all()

    context = {
            'worker_model':worker_model
            }

    return render(request,'worker_market_place.html',context)
