from django import forms
from .models import *
from apps.base.models import *
from django.contrib.auth.models import User

class DocumentForm(forms.ModelForm):    

    user_residence_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'id':'quarters'}),
        label = 'Votre résidance actuelle (Quartier/Colline) : ',
        queryset = Quarter.objects.all())

    propriety_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'id':'quarters1'}),
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