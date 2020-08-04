from django import forms
from .models import *
from apps.base.models import *
from django.contrib.auth.models import User

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
        label = 'Quartier de résidance actuel : ',
        queryset = Quarter.objects.all())

    quarter_propriety = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Quartier dans lequel se trouve la parcelle : ',
        queryset = Quarter.objects.all())

    propriety_surface = forms.FloatField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Superficie', 
                    'class': 'form-control'}),
        label = 'Superficie de votre parcelle : ')

    class Meta:
        model = Document
        fields = ("zone",'residence_quarter','quarter_propriety','propriety_surface')


