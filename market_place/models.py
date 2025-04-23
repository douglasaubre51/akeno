from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from .choices import Status

# Create your models here.


class User(models.Model):

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50)

    phone_no = models.CharField(max_length=12)
    email_id = models.EmailField(unique=True)

    place = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    profile_img = models.ImageField(upload_to = 'images/',blank = True,null = True)

class Worker(User):

    ratings = models.DecimalField(max_digits=2,decimal_places=1,blank=True,null=True)

    q1 = models.CharField(max_length=50,blank=True,null=True)
    q2 = models.CharField(max_length=50,blank=True,null=True)
    q3 = models.CharField(max_length=50,blank=True,null=True)
    q4 = models.CharField(max_length=50,blank=True,null=True)
    q5 = models.CharField(max_length=50,blank=True,null=True)

    status = models.IntegerField(choices=Status.choices,default=Status.READY)

