from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, FormView

from core.models import Terminology

from django.urls import reverse_lazy

from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.template import RequestContext

from core.filters import OrderFilter

from core.forms import AdvancedSearch

from django.db.models import Q

class IndexView(ListView):
    template_name = "index.html"
    model = Terminology
    paginate_by = 2
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = Terminology.objects.all().order_by('word')
        page = self.request.GET.get('page',1)
        paginator = Paginator(page_obj, self.paginate_by)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        context['page_obj'] = page_obj
        context['myFilter'] = OrderFilter(self.request.GET, request=page_obj)
        myFilter = OrderFilter(self.request.GET, request=page_obj)
        page_obj = myFilter.qs
        context['page_obj'] = page_obj
        return context

class SearchResultsView(ListView):
    model = Terminology
    paginate_by = 10
    template_name = 'search.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if(query==None):#lxo de codigo mas funciona
            query=""
            list_terms = Terminology.objects.all().order_by('word')
        else:
            list_terms = Terminology.objects.filter(word__icontains = query).order_by('word')
        query2 = self.request.GET.get('k')
        if(self.request.GET.get('k') != None):
            list_terms = Terminology.objects.filter(Q(word__icontains = query) & Q(area = query2))
        teste = list_terms.count()
        page = self.request.GET.get('page',1)
        paginator = Paginator(list_terms, self.paginate_by)#Não entendi mt bem a paginação, mas funciona (em partes)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        context['page_obj'] = page_obj
        context['quant']    = list_terms.count()
        context['search']   = query 
        context['category']   = query2  
        return context
class WordDetailView(DetailView):
    template_name = 'details.html'
    model =Terminology
class ErrorView(DetailView):
    template_name = 'sorry.html'
class AboutView(TemplateView):
    template_name = 'about.html'


# Create your views here.
