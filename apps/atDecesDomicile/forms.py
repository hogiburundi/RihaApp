from django import forms
from .models import *
from apps.base.models import *
from datetime import date

class DocumentForm(forms.ModelForm):

    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Zone', 
                    'class': 'form-control', 
                    'list':'zones'}),
        label = 'Zone de residence actuelle',
        queryset = Zone.objects.all())

    dead_man =  forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': "Nom Défunt", 
                    'class': 'form-control',
                    'list':'profiles'}),
        label = "Nom complet du Défunt",
        queryset = Profile.objects.all())
    

    residence_quarter_DM = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Quartier de residence actuelle',
        queryset = Quarter.objects.all())

    DM_date = forms.DateField(widget=forms.TextInput(
            attrs={'placeholder':'date delivrated ', 'type':'date',
                'class':'form-control',}),
        label='Date et heure de décès :', required=False,initial=date.today())

    first_witness = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Temoin', 
                    'class': 'form-control', 
                    'list':'profiles'}),
        label = "1er Témoin",
        queryset =Profile.objects.all())

    second_witness = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Temoin', 
                    'class': 'form-control', 
                    'list':'profiles'}),
        label = "2ème Témoin",
        queryset =Profile.objects.all())

    class Meta:
        model = Document
        # fields = ("zone_leader", "zone", "beneficiary", "father", "mother", "birth_quarter", "birth_year", "birth_commune", "birth_province", "nationality", "etat_civil", "proffession", "residence_quarter", "residence_zone", "CNI", "payment_method", "payment_serial")
        fields = ("zone", "dead_man","residence_quarter_DM","DM_date",
            "first_witness","second_witness")






