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

    beneficiary = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary CNI', 
                    'class': 'form-control'}),
        label = 'Beneficiary CNI')

    beneficiary_residence_zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Beneficiary residence zone', 
                    'class': 'form-control',
                    'id':'beneficiary_residence_zone'}),
        label='Beneficiary residence zone',
        queryset = Zone.objects.all()) 

    property_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Property quarter', 
                    'class': 'form-control',
                    'id':'property_quarter'}),
        label='Property quarter',
        queryset = Quarter.objects.all())

    beneficiary_residence_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Beneficiary residence quarter', 
                    'class': 'form-control',
                    'id':'beneficiary_residence_quarter'}),
        label='Beneficiary residence quarter',
        queryset = Quarter.objects.all())

    mrs = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver wife name', 
                    'class': 'form-control'}),
        label = 'Giver wife name')

    witness11 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver witness name',
                    'id':'', 
                    'class': 'form-control'}),
        label = 'Giver witness name 1')    
           
    witness12 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver witness name',
                    'id':'', 
                    'class': 'form-control'}),
        label = 'Giver witness name 2')
        
    witness21 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary witness name',
                    'id':'', 
                    'class': 'form-control'}),
        label = 'Beneficiary witness 1')

    witness22 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary witness name',
                    'id':'', 
                    'class': 'form-control'}),
        label = 'Beneficiary witness 2')

    cnis11 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver witness CNI',
                    'id':'', 
                    'class': 'form-control'}),
        label = 'Giver witness CNI 1')  
              
    cnis12 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver witness CNI',
                    'id':'', 
                    'class': 'form-control'}),
        label = 'Giver witness CNI 2')
        
    cnis21 = forms.CharField( 
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary witness CNI',
                    'id':'', 
                    'class': 'form-control'}),
        label = 'Beneficiary witness CNI 1')

    cnis22 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary witness CNI',
                    'id':'', 
                    'class': 'form-control'}),
        label = 'Beneficiary witness CNI 2')

    giver_witness_residence1 = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Giver witness residence',
                    'id':'giver_witness_residence1', 
                    'class': 'form-control'}),
        label='Giver witness residence 1',
        queryset = Quarter.objects.all())  
              
    giver_witness_residence2 = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Giver witness residence',
                    'id':'giver_witness_residence2', 
                    'class': 'form-control'}),
        label='Giver witness residence 2',
        queryset = Quarter.objects.all())
        
    beneficiary_witness_residence1 = forms.ModelChoiceField( 
        widget = forms.Select(
            attrs = {'placeholder': 'Beneficiary witness residence',
                    'id':'beneficiary_witness_residence1', 
                    'class': 'form-control'}),
        label='Beneficiary witness residence 1',
        queryset = Quarter.objects.all())

    beneficiary_witness_residence2 = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Beneficiary witness residence',
                    'id':'beneficiary_witness_residence2', 
                    'class': 'form-control'}),
        label='Beneficiary witness residence 2',
        queryset = Quarter.objects.all())
        

    class Meta:
        model = Document
        fields = ("residence_quarter", "zone", "beneficiary", "beneficiary_residence_quarter",
        "beneficiary_residence_zone", "property_quarter",
        "mrs","witness11","witness12","witness22","witness21",
        "cnis11","cnis12","cnis21","cnis22", "giver_witness_residence1",
        "giver_witness_residence2","beneficiary_witness_residence1","beneficiary_witness_residence2")



