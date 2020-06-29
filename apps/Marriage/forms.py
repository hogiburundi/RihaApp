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
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Residence Quarter')


    age_epoux = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Tapez l\'age  en lettre' , 
                    'class': 'form-control'}),
            label = 'age epoux') 
    age_epouse = forms.CharField(
            widget = forms.TextInput(
                attrs = {'placeholder': 'Tapez l\'age  en lettre' , 
                        'class': 'form-control'}),
                label = 'age epouse') 

    nom_prenom_epouse= forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'nom et prenom de l\'epouse' , 
                    'class': 'form-control'}),
            label = 'nom et prenom de l\'epouse')

    nom_prenom_pere_epouse  = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'nom et prenom du pere d l\'epouse' , 
                    'class': 'form-control'}),
            label = 'nom et prenom du pere d l\'epouse')
    nom_prenom_mere_epouse  = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'nom et prenom du mere d l\'epouse' , 
                    'class': 'form-control'}),
            label = 'nom et prenom du mere')

    job_epouse         = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'job' , 
                    'class': 'form-control'}),
            label = 'job')
    residence_epouse   = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'residence' , 
                    'class': 'form-control'}),
            label = 'Residence')
    # nationalite_epouse = forms.CharField(
    #     widget = forms.TextInput(
    #         attrs = {'placeholder': 'nationalite' , 
    #                 'class': 'form-control'}),
    #         label = 'Nationalite de l\'epouse')

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
        

    class Meta:
        model = Document
        fields = (
            "zone",
             "residence_quarter",
             "year",
             "jour",
             "mois",
             "age_epoux",
             "age_epouse",
             "nom_prenom_epouse",
             "nom_prenom_pere_epouse",
             "nom_prenom_mere_epouse",
             "job_epouse",
             "residence_epouse"
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