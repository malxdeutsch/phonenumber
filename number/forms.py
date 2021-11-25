from django import forms
from phonenumber_field.formfields import PhoneNumberField

class HomepageForm(forms.Form):
    name = forms.CharField(max_length = 200, required= False)
    phone_number= PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('Phone')}), required=False)