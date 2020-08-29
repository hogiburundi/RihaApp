from django import forms
from .models import *
from apps.base.models import *
from django.contrib.auth.models import User

class DocumentForm(forms.ModelForm):    
    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Zone', 
                    'class': 'form-control', 
                    'id':'zones'}),
        label = 'Zone',
        queryset = Zone.objects.all())

    quarter_propriety = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'id':'quarters'}),
        label = 'Quartier dans lequel se trouve la parcelle : ',
        queryset = Quarter.objects.all())

    propriety_surface = forms.FloatField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Superficie', 
                    'class': 'form-control'}),
        label = 'Superficie de votre parcelle : ')

    class Meta:
        model = Document
        fields = ("zone",'quarter_propriety','propriety_surface')


class ValidationForm(forms.Form):
    cni_recto = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image recto '}),
        label='image recto', required=False)
    cni_verso = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image verso '}),
        label='image verso', required=False)
    payment = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'le code de paiement '}),
        label='le code de paiement', required=False)
    cni = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'numero CNI '}),
        label='numero CNI', required=False)