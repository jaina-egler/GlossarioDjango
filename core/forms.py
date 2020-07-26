from django import forms
from core.models import Terminology

class AdvancedSearch(forms.ModelForm):
    class Meta:
        model = Terminology
        fields = ('area', 'word')
      