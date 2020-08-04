from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):
    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Zone', 'class': 'form-control', 'id':'zones'}),
        label = 'Zone',
        queryset = Zone.objects.all())
    
    residence_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 'class': 'form-control','id':'quarters'}),
        label = 'Residence Quarter',
        queryset = Quarter.objects.all())

    conjoint    = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder' : 'Le numero de Cni epoux/epouse',
                     'class': 'form-control'}),
        label = 'Conjoint')


    date = forms.DateField(
        widget = forms.SelectDateWidget(
            attrs = {'placeholder': 'date' , 
                    'class': 'form-control',
                    'style': 'display:inline-block; width: auto'}),
            label = 'date')

            
    acte = forms.IntegerField(
            widget = forms.NumberInput(
                attrs = {'placeholder': 'numero d\'acte' , 
                        'class': 'form-control'}),
                label = 'Acte')

            
    volume = forms.IntegerField(
            widget = forms.NumberInput(
                attrs = {'placeholder': 'numero de volume', 
                        'class': 'form-control'}),
                label = 'Volume')


    class Meta:
        model = Document
        fields = (
            "zone",
             "residence_quarter",
             'acte',
             'volume',
             'conjoint',
             'date'
            )




    def clean_conjoint(self, *arg, **kwargs):
        try:
            CNI = self.cleaned_data.get('conjoint')
            conjoint = Profile.objects.get(CNI = CNI)
            return conjoint
        except Exception as e:
            raise forms.ValidationError("Desolee, le conjoint  n'existe pas!! ")