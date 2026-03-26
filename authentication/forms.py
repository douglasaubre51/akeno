from django import forms

from .models import Account,Worker

class SignupForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = [
                'username',
                'password',
                'email',
                'first_name',
                'last_name',
                'profile_img',
                'phone_no',
                'place',
                'state',
                'country'
        ]

class WorkerSignupForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = [
                'username',
                'password',
                'email',
                'first_name',
                'last_name',
                'profile_img',
                'phone_no',
                'place',
                'state',
                'country',
                'q1',
                'q2',
                'q3',
                'q4',
                'q5'
        ]
