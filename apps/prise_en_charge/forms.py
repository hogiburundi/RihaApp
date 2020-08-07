from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):
    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Zone', 
                    'class': 'form-control',
                    'id':'zone'}),
        label = 'Residence Zone',
        queryset = Zone.objects.all())
        
    residence_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'id':'residence_quarter'}),
        label = 'Residence Quarter',
        queryset = Quarter.objects.all())

    mr = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Taker in charge (Mr.)', 
                    'class': 'form-control'}),
        label = 'Taker in charge (Mr.)')

    mrs = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Wife of taker in charge(Mrs.)', 
                    'class': 'form-control'}),
        label = 'Wife of taker in charge (Mrs.)')

    mr_mrs_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Takers in charge Residence Quarter', 
                    'class': 'form-control',
                    'id':'mr_mrs_quarter'}),
        label = 'Takers in charge Residence Quarter',
        queryset = Quarter.objects.all())


    class Meta:
        model = Document
        fields = ("zone", "residence_quarter","mr","mrs","mr_mrs_quarter")