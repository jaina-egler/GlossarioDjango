from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, FormView

from core.models import Glossario


from django.urls import reverse_lazy

from django.contrib import messages

from django.core.paginator import Paginator

from django.template import RequestContext

class IndexView(ListView):
    template_name = "index.html"
    model = Glossario
    paginate_by = 10

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
    template_name = 'details.html'
    model = Glossario
class ErrorView(DetailView):
    template_name = 'sorry.html'
    model = Glossario




# Create your views here.
