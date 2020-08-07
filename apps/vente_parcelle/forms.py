from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):
    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Zone', 
                    'class': 'form-control', 
                    'id':'zone'}),
        label='Residence Zone',
        queryset = Zone.objects.all())
        
    residence_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'id':'residence_quarter'}),
        label='Residence Quarter',
        queryset = Quarter.objects.all())

    amount = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Amount', 
                    'class': 'form-control'}),
        label = 'Amount')
        
    # cellule = forms.CharField(
    #     widget = forms.TextInput(
    #         attrs = {'placeholder': 'Cellule', 
    #                 'class': 'form-control'}),
    #     label = 'Cellule')

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

    buyer_zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Buyer Zone', 
                    'class': 'form-control',
                    'id':'buyer_zone'}),
        label='Buyer Residence Zone',
        queryset = Zone.objects.all())
    
    buyer_residence_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Buyer Residence Quarter', 
                    'class': 'form-control',
                    'id':'buyer_residence_quarter'}),
        label='Buyer Residence Quarter',
        queryset = Quarter.objects.all())

    witness11 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Saler witness name 1',
                    'class': 'form-control'}),
        label = 'Saler witness name 1')    
           
    witness12 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Saler witness name 2',
                    'class': 'form-control'}),
        label = 'Saler witness name 2')
        
    witness21 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer witness name 1',
                    'class': 'form-control'}),
        label = 'Buyer witness name 1')

    witness22 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer witness name 2',
                    'class': 'form-control'}),
        label = 'Buyer witness name 2')

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

    saler_witness_residence1 = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Saler witness residence 1',
                    'id':'saler_witness_residence1', 
                    'class': 'form-control'}),
        label = 'Saler witness residence 1',
        queryset = Zone.objects.all())  
              
    saler_witness_residence2 = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Saler witness residence 2',
                    'id':'saler_witness_residence2', 
                    'class': 'form-control'}),
        label = 'Saler witness residence 2',
        queryset = Zone.objects.all())
        
    buyer_witness_residence1 = forms.ModelChoiceField( 
        widget = forms.Select(
            attrs = {'placeholder': 'Buyer witness residence 1',
                    'id':'buyer_witness_residence1', 
                    'class': 'form-control'}),
        label = 'Buyer witness residence 1',
        queryset = Zone.objects.all())

    buyer_witness_residence2 = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Buyer witness residence 2',
                    'id':'buyer_witness_residence2', 
                    'class': 'form-control'}),
        label='Buyer witness residence 2',
        queryset = Zone.objects.all())

    class Meta:
        model = Document
        fields = ("residence_quarter", "zone", "property_quarter", "amount", "buyer",
        "buyer_residence_quarter", "buyer_zone", "witness11", "witness12", "witness21",
        "witness22", "cnis11", "cnis12", "cnis21", "cnis22", "saler_witness_residence1",
        "saler_witness_residence2","buyer_witness_residence1","buyer_witness_residence2")
