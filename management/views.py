from django.shortcuts import render

from django.views.generic import TemplateView

class AdminMenuView(TemplateView):
    template_name = 'menu.html'
# Create your views here.
