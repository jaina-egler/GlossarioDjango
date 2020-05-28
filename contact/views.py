from django.views.generic import CreateView
from django.shortcuts import render

from django.urls import reverse_lazy

from django.contrib import messages

from contact.forms import ContactForm

class ContactFormView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    def form_valid(self, form):
        messages.success(self.request, "Email enviado com sucesso")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao preencher formulário")
        return super().form_invalid(form)
# Create your views here.
