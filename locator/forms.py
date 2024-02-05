from django import forms
from django.core.validators import RegexValidator


class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(
        label="Enter phone number",
        validators=[
            RegexValidator(
                regex=r"^\d{11}$",
                message="Phone number must be 11 digits.",
                code="invalid_phone_number",
            )
        ],
    )
