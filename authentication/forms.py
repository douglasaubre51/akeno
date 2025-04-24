from django import forms

from .models import Account

class SignupForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['username','password','email','first_name','last_name','profile_img','phone_no','place','state','country']
