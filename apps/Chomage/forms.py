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
    anneeEnChomage = forms.IntegerField( 
        widget=forms.NumberInput(
            attrs={'placeholder':'Depuis quand en chomage  ',
                    'class':'form-control'}),
        label='Annee')


    class Meta:
        model = Document
        fields = ("zone", "residence_quarter", 'anneeEnChomage')

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