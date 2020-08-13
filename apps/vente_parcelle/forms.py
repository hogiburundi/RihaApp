from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):

    amount = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Amount', 
                    'class': 'form-control'}),
        label = 'Amount')

    property_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Property Quarter', 
                    'class': 'form-control',
                    'id':'property_quarter'}),
        label='Property Quarter',
        queryset = Quarter.objects.all())
        
    buyer = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer CNI', 
                    'class': 'form-control'}),
        label = 'Buyer CNI')

    cnis11 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Saler witness CNI 1',
                    'class': 'form-control'}),
        label = 'Saler witness CNI 1')  
              
    cnis12 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Saler witness CNI 2',
                    'class': 'form-control'}),
        label = 'Saler witness CNI 2')
        
    cnis21 = forms.CharField( 
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer witness CNI 1',
                    'class': 'form-control'}),
        label = 'Buyer witness CNI 1')

    cnis22 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer witness CNI 2',
                    'class': 'form-control'}),
        label = 'Buyer witness CNI 2')
        
    search_place = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Place to look for the document.', 
                    'class': 'form-control',
                    'id':'search_place'}),
        label = 'Place to look for the document.',
        queryset = Quarter.objects.all())

    class Meta:
        model = Document
        fields = ("search_place", "property_quarter", "amount", "buyer", "cnis11", "cnis12", "cnis21", "cnis22")

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