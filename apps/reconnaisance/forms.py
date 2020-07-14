from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):
    zone = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Work Zone', 
                    'class': 'form-control', 
                    'list':'zones'}),
        label = 'Work Zone')
    residence_quarter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Work Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Work Quarter')
        
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

    def clean_zone(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("zone")
            zone = Zone.objects.get(name=name)
            return zone
        except:
            raise forms.ValidationError("this zone is unknown")

    def clean_residence_quarter(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("residence_quarter").split()[0]
            zone = self.cleaned_data.get("residence_quarter").split()[-1]
            quarter = Quarter.objects.get(name=name, zone__name=zone)
            return quarter
        except Exception as e:
            raise forms.ValidationError("this quarter is unknown")