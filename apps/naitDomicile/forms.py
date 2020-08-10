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

    child_name =  forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': "Nom Enfant", 
                    'class': 'form-control',}),
        label = "Nom complet de l'enfant")

    child_birth = forms.DateField(widget=forms.TextInput(
            attrs={'placeholder':'date delivrated ', 'type':'date',
                'class':'form-control',}),
        label='Date de naissance enfant :', required=False,initial=date.today())

    child_birth_quarter = forms.ModelChoiceField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Quartier naissance', 
                    'class': 'form-control', 
                    'id':'quarters'}),
        label = "Quartier de naissance de l'enfant",
        queryset = Quarter.objects.all())

    child_mother = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Mère', 
                    'class': 'form-control', 
                    'id':'profiles'}),
        label = "Mère de l'enafant",
        queryset = Profile.objects.all())

    first_witness = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Témoin 1', 
                    'class': 'form-control', 
                    'id':'profiles1'}),
        label = "Temoins 1 : ",
        queryset = Profile.objects.all())

    second_witness = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Temoin 2', 
                    'class': 'form-control', 
                    'id':'profiles2'}),
        label = "Témoin 2 : ",
        queryset = Profile.objects.all())

    class Meta:
        model = Document
        # fields = ("zone_leader", "zone", "beneficiary", "father", "mother", "birth_quarter", "birth_year", "birth_commune", "birth_province", "nationality", "etat_civil", "proffession", "residence_quarter", "residence_zone", "CNI", "payment_method", "payment_serial")
        fields = ("zone","child_name","child_birth","child_birth_quarter",
            "child_mother","first_witness","second_witness")


class ValidationForm(forms.Form):
    cni_recto_declarant = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'Votre CNI recto '}),
        label='Votre CNI recto', required=False)
    cni_verso_declarant = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'Votre CNI verso '}),
        label='Votre CNI verso ', required=False)
    cni_declarant = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'Votre CNI '}),
        label='Votre CNI', required=False)

    cni_recto_1_temoin = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'CNI recto temoin1 '}),
        label='CNI recto temoin1', required=False)
    cni_verso_1_temoin = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'CNI verso temoin1 '}),
        label='CNI verso temoin1', required=False)
    cni_1_temoin = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':' CNI temoin1 '}),
        label='CNI temoin1', required=False)

    cni_recto_2_temoin = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'CNI recto temoin2 '}),
        label='CNI recto temoin2', required=False)
    cni_verso_2_temoin = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'CNI verso temoin2 '}),
        label='CNI verso temoin2', required=False)
    cni_2_temoin = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'CNI temoin2 '}),
        label='CNI temoin2', required=False)

    # payment = forms.BooleanField(
    #     widget=forms.CheckboxInput(attrs={'placeholder':'le code de paiement '}),
    #     label='le code de paiement', required=False)
    
    
    

