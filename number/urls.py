from django.urls import path
from .views import phonenumber, name , homepage

urlpatterns = [
    path('phone_number/<str:phone_number>', phonenumber, name = 'phonenumber'),
    path('name/<str:name>', name, name = 'name'),
    path('homepage/', homepage, name = 'homepage')
]
