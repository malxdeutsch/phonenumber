from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Person (models.Model):
    name = models.CharField(max_length = 200)
    email= models.CharField(max_length = 200)
    phone_number= PhoneNumberField(null=False, blank=False, unique=True)
    address = models.CharField(max_length = 200)