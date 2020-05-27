from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, FormView

from core.models import Glossario

from core.forms import ContactForm

from django.urls import reverse_lazy

from django.contrib import messages

from django.shortcuts import render_to_response

from django.template import RequestContext

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['todos'] = Glossario.objects.all()
            return context

class SearchResultsView(ListView):
    model = Glossario
    template_name = 'search.html'
    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        context['object_list'] = Glossario.objects.filter(word__icontains=query)
        context['quant'] = Glossario.objects.filter(word__icontains=query).count()
        context['query2'] = query
        return context
class WordDetailView(DetailView):
    template_name = 'word.html'
    model = Glossario
class ErrorView(DetailView):
    template_name = 'sorry.html'
    model = Glossario
class ContactFormView(FormView):
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
