from django.urls import path, include
from core.views import IndexView, SearchResultsView, WordDetailView,  ErrorView,  AboutView

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('search', SearchResultsView.as_view(), name='search'),
    path('word/<int:pk>/<slug:slug>',WordDetailView.as_view(), name='word' ),
    path('404', ErrorView.as_view(), name= 'error'),
    path('about', AboutView.as_view(),name='about'),
    path('', include('contact.urls')),
    path('', include('management.urls')),
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)#acesso aos arquivos de midia nos templates