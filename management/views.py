from django.views.generic import TemplateView, CreateView, DeleteView, ListView, UpdateView
from django.shortcuts import render

from django.urls import reverse_lazy

from django.contrib import messages

from management.forms import AddTermForm

from core.models import Terminology

from contact.models import Contact

from django.contrib.auth.mixins import LoginRequiredMixin       
class AdminMenuView(LoginRequiredMixin,TemplateView):
    template_name = 'menu.html'


class UpdateTermView(LoginRequiredMixin,UpdateView):
    template_name = 'update.html'
    form_class = AddTermForm
    success_url = reverse_lazy('update')
    def form_valid(self, form):
        messages.success(self.request, "Terminologia atualizada com sucesso")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao preencher atualizar terminologia")
        return super().form_invalid(form)

class AddTermView(LoginRequiredMixin,CreateView):
    template_name = 'add.html'
    form_class = AddTermForm
    success_url = reverse_lazy('add')
    def form_valid(self, form):
        messages.success(self.request, "Terminologia adicionada com sucesso")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao preencher adicionar terminologia")
        return super().form_invalid(form)

class AllTermsView(LoginRequiredMixin,ListView):
    model = Terminology
    template_name = 'all.html'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['all'] = Terminology.objects.all().order_by('word')
            return context

class DetailsTermView(LoginRequiredMixin,ListView):
    model = Terminology
    template_name = 'detailTerm.html'
class DeleteTermView(LoginRequiredMixin,DeleteView):
    model = Terminology
    context_object_name = 'term'
    template_name = 'delete.html'
    success_url = reverse_lazy('all')

class AllMessagesView(LoginRequiredMixin,ListView):
    model = Contact
    template_name = 'seeContacts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all'] = Contact.objects.all().order_by('-sendAt')
        return context
class DetailsMessageView(LoginRequiredMixin,ListView):
    model = Terminology
    template_name = 'seeContacts.html'
# Create your views here.
