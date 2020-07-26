from django.contrib import admin
from core.models import Terminology
from contact.models import Contact
from django.template.defaultfilters import slugify

admin.site.register(Terminology)

admin.site.register(Contact)
# Register your models here.
