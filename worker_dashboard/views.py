from django.shortcuts import render

# Create your views here.
def get_worker_dashboard_page(request):
    return render(
            request,
            'worker-dashboard.html'
            )
