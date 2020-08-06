from django import forms
from .models import *
from django.forms import formset_factory
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


    sous_couvert = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'sous couvert', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Sous couvert')

    class Meta:
        model = Document
        fields = ("zone", "residence_quarter", 'sous_couvert')






    def sous_couvert (self, *arg, **kwargs):
        try:
            CNI = self.cleaned_data.get('sous_couvert')
            sous_couvert = Profile.objects.get(CNI = CNI)
            return sous_couvert
        except Exception as e:
            raise forms.ValidationError("Desolee, le temoin  n'existe pas!! ")