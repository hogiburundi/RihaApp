from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):    
    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Zone', 
                    'class': 'form-control', 
                    'list':'zones'}),
        label = 'Zone',
        queryset = Zone.objects.all())
    
    residence_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Residence Quarter',
        queryset = Quarter.objects.all())

    class Meta:
        model = Document
        fields = ("zone", "residence_quarter")

    # def clean_zone(self, *arg,**kwargs):
    #     try:
    #         name = self.cleaned_data.get("zone")
    #         zone = Zone.objects.get(name=name)
    #         return zone
    #     except:
    #         raise forms.ValidationError("this zone is unknown")

    # def clean_residence_quarter(self, *arg,**kwargs):
    #     try:
    #         name = self.cleaned_data.get("residence_quarter").split()[0]
    #         zone = self.cleaned_data.get("residence_quarter").split()[-1]
    #         quarter = Quarter.objects.get(name=name, zone__name=zone)
    #         return quarter
    #     except Exception as e:
    #         raise forms.ValidationError("this quarter is unknown")

