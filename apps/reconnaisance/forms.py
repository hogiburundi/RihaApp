from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):
        
    residence_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Work Quarter', 
                    'class': 'form-control',
                    'id':'residence_quarter'}),
        label = 'Work Quarter',
        queryset = Quarter.objects.all())
        
    association = forms.CharField(
        widget = forms.TextInput(
        attrs = {'placeholder': 'Votre Association', 
                    'class': 'form-control'}),
        label = 'Votre Association')

    start_year = forms.CharField(
        widget = forms.TextInput(
        attrs = {'placeholder': 'Année de lancement', 
                    'class': 'form-control'}),
        label = 'Année de lancement')    
    
    class Meta:
        model = Document
        fields = ("residence_quarter", "association", "start_year")
        
class ValidationForm(forms.Form):
    cni_recto = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI recto', required=False)
    cni_verso = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI verso', required=False)
    cni_recto_1 = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI recto comparant 1', required=False)
    cni_verso_1 = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI verso comparant 1', required=False)
    cni_recto_2 = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI recto comparant 2', required=False)
    cni_verso_2 = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI verso comparant 2', required=False)
    payment = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'le code de paiement '}),
        label='le code de paiement', required=False)
    cni = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'numero CNI '}),
        label='numero CNI', required=False)