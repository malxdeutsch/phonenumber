from django.shortcuts import render
from .models import Person

# Create your views here.

def phonenumber (request, phone_number):
    person = Person.objects.get(phone_number = phone_number)
    return render(request, 'phonenumber.html', {'person':person})
    
def name (request, name):
    person = Person.objects.get(name = name)
    return render(request, 'name.html', {'person':person})