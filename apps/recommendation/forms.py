from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):    
    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Zone de recuperation du document', 
                    'class': 'form-control', 
                    'list':'zones'}),
        label = 'Zone',
        queryset = Zone.objects.all())

    work_doc_copy = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'placeholder':'Contrat',
                'class':'form-control'}),
            label='Contrat')
    

    class Meta:
        model = Document
        # fields = ("zone_leader", "zone", "beneficiary", "father", "mother", "birth_quarter", "birth_year", "birth_commune", "birth_province", "nationality", "etat_civil", "proffession", "residence_quarter", "residence_zone", "CNI", "payment_method", "payment_serial")
        fields = ("zone", 'work_doc_copy')

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
    work_doc_copy = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'contrat d\'execution d\'un travail quelconque '}),
        label='contrat', required=False)