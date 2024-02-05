from django import forms


class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(label="Enter phone number")
