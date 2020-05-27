from django import forms

from django.core.mail.message import EmailMessage

class ContactForm(forms.Form):
    name = forms.CharField(label="Nome", max_length = 100)
    email = forms.CharField(label="Email", max_length = 100)
    topic = forms.CharField(label="Tópico", max_length = 50)
    message = forms.CharField(label="Mensagem", max_length = 300, widget = forms.Textarea)