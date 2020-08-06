from django import forms
from .models import *
from apps.base.models import *
from datetime import date

class DocumentForm(forms.ModelForm):
    bride = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Bride', 
                    'class': 'form-control', 
                    'list':'profiles'}),
        label = 'Bride',
        queryset = Profile.objects.all())

    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Zone', 
                    'class': 'form-control', 
                    'list':'zones'}),
        label = 'Zone',
        queryset = Zone.objects.all())


    residence_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Residence Quarter',
        queryset = Quarter.objects.all())

    date = forms.DateField(widget=forms.TextInput(
            attrs={'placeholder':'date delivrated ', 'type':'date',
                'class':'form-control',}),
        label='Date d\'etat civil :', required=False,initial=date.today())

    class Meta:
        model = Document
        fields = ("zone", "bride", "residence_quarter", 'date')
