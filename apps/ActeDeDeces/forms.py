from django import forms
from .models import *
from apps.base.models import *


etat_civil = (
    ("Celibataire", 'Celibataire'),
    ("Marie", "Marie")
)

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
    etat_civil = forms.ChoiceField(
        widget=forms.Select(
            attrs={'placeholder':'etatcivil ','class':'form-control'}),
        label='Etat Civil',
        choices=etat_civil)

    age = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'age en lettre ','class':'form-control'}), label='Age du defunt')
    annee = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'annee en lettre ','class':'form-control'}), label='Annee')
    jour = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'jour en lettre ','class':'form-control'}), label='Jour')
    mois = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'mois en lettre ','class':'form-control'}), label='Mois')

    

    class Meta:
        model = Document
        fields = ("zone", "residence_quarter", "etat_civil",'annee', 'jour', 'mois', "age" )

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