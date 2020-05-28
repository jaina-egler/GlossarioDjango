from django import forms

from django.core.mail.message import EmailMessage

from contact.models import Contact

class ContactForm(forms.ModelForm):
   class Meta:
        model = Contact
        fields = ['name','email','subject','message']