from django import forms

from core.models import Glossario

class AddTermForm(forms.ModelForm):
   class Meta:
        model = Glossario
        fields = ['image','word','area','expression','definition']