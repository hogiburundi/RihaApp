from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):

    mr = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Taker in charge(Mr.)', 
                    'class': 'form-control'}),
        label = 'Taker in charge (Mr.)')
        
    mrs = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Wife of taker in charge(Mrs.)', 
                    'class': 'form-control'}),
        label = 'Wife of taker in charge (Mrs.)')

    search_place = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Place to look for the document.', 
                    'class': 'form-control',
                    'id':'search_place'}),
        label = 'Place to look for the document.',
        queryset = Quarter.objects.all())


    class Meta:
        model = Document
        fields = ("search_place","mr","mrs")

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
        