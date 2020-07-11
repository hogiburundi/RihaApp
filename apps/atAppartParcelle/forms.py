from django import forms
from .models import *
from apps.base.models import *
from django.contrib.auth.models import User

class DocumentForm(forms.ModelForm):    

    user_residence_quarter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Votre résidance actuelle (Quartier/Colline) : ')

    propriety_quarter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Emplacement de la pacelle (Quartier/Colline) : ')

    propriety_surfaces_a = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Ares', 
                    'class': 'form-control'}),
        label = "Surface de la parcelle ")

    propriety_contenency = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Maison, Cultures, Arbres, etc ...', 
                    'class': 'form-control'}),
        label = "Contenance de votre parcelle : ")


    class Meta:
        model = Document
        fields = ("user_residence_quarter", "propriety_quarter", "propriety_surfaces_a","propriety_contenency")


    def clean_user_residence_quarter(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("user_residence_quarter").split()[0]
            zone = self.cleaned_data.get("user_residence_quarter").split()[-1]
            quarter = Quarter.objects.get(name=name, zone__name=zone)
            return quarter
        except Exception as e:
            raise forms.ValidationError("this quarter is unknown")

    def clean_propriety_quarter(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("propriety_quarter").split()[0]
            zone = self.cleaned_data.get("propriety_quarter").split()[-1]
            quarter = Quarter.objects.get(name=name, zone__name=zone)
            return quarter
        except Exception as e:
            raise forms.ValidationError("this quarter is unknown")
