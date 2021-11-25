from django.shortcuts import render, redirect
from .models import Person
from .forms import HomepageForm

# Create your views here.

def phonenumber(request, phone_number):
    person = Person.objects.get(phone_number = phone_number)
    return render(request, 'phonenumber.html', {'person':person})
    
def name(request, name):
    person = Person.objects.get(name = name)
    return render(request, 'name.html', {'person':person})

def homepage(request):
    if request.method == 'POST':
        form = HomepageForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['name']:
                search_name = Person.objects.get(name = form.cleaned_data['name'])
                return redirect('name', search_name.name)
            if form.cleaned_data['phone_number']:
                search_phone = Person.objects.get(name = form.cleaned_data['phone_number'])
                return redirect('phonenumber', search_name.phone_number)

    if request.method == 'GET':
        form = HomepageForm()
    return render(request, 'homepage.html', {'form': form})

