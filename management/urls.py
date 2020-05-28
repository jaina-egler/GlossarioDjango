from django.urls import path

from management.views import AdminMenuView

urlpatterns = [
    path('management/',AdminMenuView.as_view(),name='management')
]#acesso aos arquivos de midia nos templates
