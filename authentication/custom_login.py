from django.contrib.auth.views import LoginView

from .models import Worker

class TwoWayLogin(LoginView):
    def get_success_url(self):
        user = self.request.user

        try:
            account = Worker.objects.get(username = user.username)

        except Worker.DoesNotExist:
            return '/dashboard/'

        return '/worker_dashboard/'
