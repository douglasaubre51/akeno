from django.shortcuts import render
from django.http import JsonResponse

import json

# Create your views here.
# sign in
def signIn(request):
    if request.method == 'POST':
        # unpack
        email = request.POST['email']
        password = request.POST['password']

        if email == None or password == None:
            message = { message: 'empty fields!' }
            return JsonResponse(
                    request,
                    message,
                    status = 400
                    )

        print(f'user logged in {email} : {password}')
        return

def signUp(request):
    pass
def signOut(request):
    pass
