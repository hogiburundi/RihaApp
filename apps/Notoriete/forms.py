from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):
    zone = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Zone', 
                    'class': 'form-control', 
                    'list':'zones'}),
        label = 'Zone') 

    residence_quarter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Quarter residence', 
                    'class': 'form-control', 
                    'list':'quarterS'}),
        label = 'Residence')

    year = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Tapez l\'annee  en lettre' , 
                    'class': 'form-control'}),
            label = 'Year') 

    jour = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Tapez le quantieme jour du mois en lettre' , 
                    'class': 'form-control'}),
            label = 'Jour')    

    mois = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Tapez le mois en lettre' , 
                    'class': 'form-control'}),
            label = 'Mois')
        
    nom_prenom_1ercomparant = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Nom et Prenom du comparant', 
                    'class': 'form-control'}),
        label = 'nom et prenom du comparant') 

    nom_prenom_1ercomparant_anneDeNaissance = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'ex: 2020', 
                    'class': 'form-control'}),
        label = 'Son annee de naissance')
    
    nom_prenom_1ercomparant_pere = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Pere du comparant', 
                    'class': 'form-control'}),
        label = 'Nom et prenom du mere du comparant')
  
    nom_prenom_1ercomparant_mere = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Mere du comparant', 
                    'class': 'form-control'}),
        label = 'Nom et prenom du mere du comparant')

    comparant_colline_naisance = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': " colline du comparant", 
                    'class': 'form-control'}),
        label = 'colline du comparant')

    class Meta:
        model = Document
        fields = (
            "zone", 
            "residence_quarter",
            "year",
            "jour",
            "mois",
            "nom_prenom_1ercomparant",
            "nom_prenom_1ercomparant_anneDeNaissance",
            "nom_prenom_1ercomparant_pere",
            "nom_prenom_1ercomparant_mere",
            "nom_prenom_1ercomparant", 
            "comparant_colline_naisance"
        )

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