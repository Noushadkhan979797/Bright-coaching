from django import forms
from .models import Contacts

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "@gmail.com" not in email:
            raise forms.ValidationError("please enter valid gmail id")
        return email