from django import forms
from .models import filecsv

class formforcsv(forms.ModelForm):
    class Meta:
        model=filecsv
        fields=['file']
        