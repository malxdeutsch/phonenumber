from django.contrib import admin
from .models import Person, PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PhoneNumberField: {'widget': PhoneNumberInternationalFallbackWidget}
    }
admin.site.register(Person, PersonAdmin)

