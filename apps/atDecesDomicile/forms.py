from django import forms
from .models import *
from apps.base.models import *
from datetime import date

class DocumentForm(forms.ModelForm):

    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Zone', 
                    'class': 'form-control', 
                    'id':'zones'}),
        label = 'Zone de residence actuelle',
        queryset = Zone.objects.all())

    dead_man =  forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': "Nom Défunt", 
                    'class': 'form-control',
                    'id':'profiles'}),
        label = "Nom complet du Défunt",
        queryset = Profile.objects.all())

    DM_date = forms.DateField(widget=forms.TextInput(
            attrs={'placeholder':'date delivrated ', 'type':'date',
                'class':'form-control',}),
        label='Date et heure de décès :', required=False,initial=date.today())

    first_witness = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Temoin', 
                    'class': 'form-control', 
                    'id':'profiles1'}),
        label = "1er Témoin",
        queryset =Profile.objects.all())

    second_witness = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Temoin', 
                    'class': 'form-control', 
                    'id':'profiles2'}),
        label = "2ème Témoin",
        queryset =Profile.objects.all())

    class Meta:
        model = Document
        # fields = ("zone_leader", "zone", "beneficiary", "father", "mother", "birth_quarter", "birth_year", "birth_commune", "birth_province", "nationality", "etat_civil", "proffession", "residence_quarter", "residence_zone", "CNI", "payment_method", "payment_serial")
        fields = ("zone", "dead_man","DM_date",
            "first_witness","second_witness")

class ValidationForm(forms.Form):
    cni_recto = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image recto '}),
        label='image recto', required=False)
    cni_verso = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image verso '}),
        label='image verso', required=False)
    cni = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'numero CNI '}),
        label='numero CNI', required=False)

    cni_recto = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image recto témoin 1 '}),
        label='image recto témoin 1', required=False)
    cni_verso = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image verso témoin 1 '}),
        label='image verso témoin 1', required=False)
    cni = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'CNI témoin 1 '}),
        label='CNI témoin 1', required=False)

    cni_recto = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image recto témoin 2 '}),
        label='image recto témoin 2', required=False)
    cni_verso = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image verso témoin 2 '}),
        label='image verso témoin 2', required=False)
    cni = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'numero CNI '}),
        label='numero CNI', required=False)






