from django import forms
from .models import *
from apps.base.models import *
from django import forms

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

    first_witness = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'witness', 
                    'class': 'form-control', 
                    'list':'profiles'}),
        label = "Témoin 1 : ",
        queryset = Profile.objects.all())

    second_witness = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'witness', 
                    'class': 'form-control', 
                    'list':'profiles'}),
        label = "Témoin 1 : ",
        queryset = Profile.objects.all())

    class Meta:
        model = Document
        fields = ("zone", "residence_quarter", "first_witness","second_witness")
