from django import forms
from .models import *
from apps.base.models import *
from django.contrib.auth.models import User

class DocumentForm(forms.ModelForm):    

    user_residence_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Votre résidance actuelle (Quartier/Colline) : ',
        queryset = Quarter.objects.all())

    propriety_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Emplacement de la pacelle (Quartier/Colline) : ',
        queryset = Quarter.objects.all())

    propriety_surfaces_a = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': '0 ares', 
                    'class': 'form-control'}),
        label = "Surface de la parcelle ")

    propriety_surfaces_ca = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': '0 centaiares', 
                    'class': 'form-control'}),
        label = "Surface de la parcelle ")

    propriety_contenency = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Maison, Cultures, Arbres, etc ...', 
                    'class': 'form-control'}),
        label = "Contenance de votre parcelle : ")


    class Meta:
        model = Document
        fields = ("user_residence_quarter", "propriety_quarter", "propriety_surfaces_a","propriety_surfaces_ca","propriety_contenency")
