"""Glossario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('contact/',include('contact.urls'))
]

admin.AdminSite.site_header = "Administração do glossário"#define o título da página
admin.AdminSite.site_title = "Sistema glossário"#define o nome do app que aparece na tela de login do admin, o que é de grande ajuda caso você esteja desenvolvendo mais de uma aplicação django
admin.AdminSite.index_title = "Sistema glossário"#Define o nome do projeto que aparece ao já ter feito login no django admin
