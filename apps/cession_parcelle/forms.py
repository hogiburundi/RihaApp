from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):
    zone = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Residence Zone', 
                    'class': 'form-control', 
                    'list':'zones'}),
        label = 'Residence Zone')
        
    residence_quarter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Residence Quarter')

    beneficiary = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary CNI', 
                    'class': 'form-control'}),
        label = 'Beneficiary CNI')

    beneficiary_residence_zone = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary residence zone', 
                    'class': 'form-control',
                    'list':'zones'}),
        label = 'Beneficiary residence zone') 

    property_quarter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Property quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Property quarter')

    beneficiary_residence_quarter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary residence quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Beneficiary residence quarter')

    mrs = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver wife name', 
                    'class': 'form-control'}),
        label = 'Giver wife name')

    witness11 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver witness name','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Giver witness name 1')    
           
    witness12 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver witness name','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Giver witness name 2')
        
    witness21 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary witness name','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Beneficiary witness 1')

    witness22 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary witness name','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Beneficiary witness 2')

    cnis11 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver witness CNI','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Giver witness CNI 1')  
              
    cnis12 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver witness CNI','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Giver witness CNI 2')
        
    cnis21 = forms.CharField( 
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary witness CNI','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Beneficiary witness CNI 1')

    cnis22 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary witness CNI','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Beneficiary witness CNI 2')

    giver_witness_residence1 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver witness residence','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Giver witness residence 1')  
              
    giver_witness_residence2 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver witness residence','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Giver witness residence 2')
        
    beneficiary_witness_residence1 = forms.CharField( 
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary witness residence','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Beneficiary witness residence 1')

    beneficiary_witness_residence2 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary witness residence','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Beneficiary witness residence 2')
        

    class Meta:
        model = Document
        fields = ("residence_quarter", "zone", "beneficiary", "beneficiary_residence_quarter",
        "beneficiary_residence_zone", "property_quarter",
        "mrs","witness11","witness12","witness22","witness21",
        "cnis11","cnis12","cnis21","cnis22", "giver_witness_residence1",
        "giver_witness_residence2","beneficiary_witness_residence1","beneficiary_witness_residence2")

    def clean_zone(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("zone")
            zone = Zone.objects.get(name=name)
            return zone
        except:
            raise forms.ValidationError("this zone is unknown")

    def clean_residence_quarter(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("residence_quarter").split()[0]
            zone = self.cleaned_data.get("residence_quarter").split()[-1]
            quarter = Quarter.objects.get(name=name, zone__name=zone)
            return quarter
        except Exception as e:
            raise forms.ValidationError("this quarter is unknown")

    def clean_beneficiary_residence_zone(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("beneficiary_residence_zone")
            zone = Zone.objects.get(name=name)
            return zone
        except:
            raise forms.ValidationError("this zone is unknown")

    def clean_property_quarter(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("property_quarter").split()[0]
            zone = self.cleaned_data.get("property_quarter").split()[-1]
            quarter = Quarter.objects.get(name=name, zone__name=zone)
            return quarter
        except Exception as e:
            raise forms.ValidationError("this quarter is unknown")

    def clean_beneficiary_residence_quarter(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("beneficiary_residence_quarter").split()[0]
            zone = self.cleaned_data.get("beneficiary_residence_quarter").split()[-1]
            quarter = Quarter.objects.get(name=name, zone__name=zone)
            return quarter
        except Exception as e:
            raise forms.ValidationError("this quarter is unknown")