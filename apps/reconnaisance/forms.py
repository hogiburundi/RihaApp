from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):
    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Work Zone', 
                    'class': 'form-control', 
                    'id':'zone'}),
        label = 'Work Zone',
        queryset = Zone.objects.all())
        
    residence_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Work Quarter', 
                    'class': 'form-control',
                    'id':'residence_quarter'}),
        label = 'Work Quarter',
        queryset = Quarter.objects.all())
        
        
    association = forms.CharField(
        widget = forms.TextInput(
        attrs = {'placeholder': 'Votre Association', 
                    'class': 'form-control'}),
        label = 'Votre Association')

    start_year = forms.CharField(
        widget = forms.TextInput(
        attrs = {'placeholder': 'Année de lancement', 
                    'class': 'form-control'}),
        label = 'Année de lancement')    
    
    class Meta:
        model = Document
        fields = ("residence_quarter", "zone", "association","start_year")