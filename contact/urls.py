
from django.urls import path

from contact.views import ContactFormView

urlpatterns = [
    path('',ContactFormView.as_view(),name='contact')
]#acesso aos arquivos de midia nos templates
