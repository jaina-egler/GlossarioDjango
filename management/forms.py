from django import forms

from core.models import Terminology

class AddTermForm(forms.ModelForm):
   class Meta:
        model = Terminology
        fields = ['image','word','area','expression','definition']