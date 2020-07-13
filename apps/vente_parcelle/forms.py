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

    property_quarter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Property Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Property Quarter')
        
    buyer = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer CNI', 
                    'class': 'form-control'}),
        label = 'Buyer CNI')

    buyer_zone = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer Zone', 
                    'class': 'form-control',
                    'list':'zones'}),
        label = 'Buyer Residence Zone')
    
    buyer_residence_quarter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Buyer Residence Quarter')

    witness11 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Saler witness name','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Saler witness name 1')    
           
    witness12 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Saler witness name','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Saler witness name 2')
        
    witness21 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer witness name','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Buyer witness 1')

    witness22 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer witness name','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Buyer witness 2')

    cnis11 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Saler witness CNI','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Saler witness CNI 1')  
              
    cnis12 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Saler witness CNI','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Saler witness CNI 2')
        
    cnis21 = forms.CharField( 
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer witness CNI','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Buyer witness CNI 1')

    cnis22 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer witness CNI','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Buyer witness CNI 2')

    saler_witness_residence1 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Saler witness residence','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Saler witness residence 1')  
              
    saler_witness_residence2 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Saler witness residence','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Saler witness residence 2')
        
    buyer_witness_residence1 = forms.CharField( 
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer witness residence','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Buyer witness residence 1')

    buyer_witness_residence2 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer witness residence','id':'witnesses', 
                    'class': 'form-control'}),
        label = 'Buyer witness residence 2')

    class Meta:
        model = Document
        fields = ("residence_quarter", "zone", "property_quarter", "amount", "buyer",
        "buyer_residence_quarter", "buyer_zone", "witness11", "witness12", "witness21",
        "witness22", "cnis11", "cnis12", "cnis22", "cnis21", "saler_witness_residence1",
        "saler_witness_residence2","buyer_witness_residence1","buyer_witness_residence2")

    def clean_zone(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("zone")
            zone = Zone.objects.get(name=name)
            return zone
        except:
            raise forms.ValidationError("this zone is unknown")

    def clean_buyer_zone(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("buyer_zone")
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
        
    def clean_buyer_residence_quarter(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("buyer_residence_quarter").split()[0]
            zone = self.cleaned_data.get("buyer_residence_quarter").split()[-1]
            quarter = Quarter.objects.get(name=name, zone__name=zone)
            return quarter
        except Exception as e:
            raise forms.ValidationError("this quarter is unknown") 
    
    def clean_property_quarter(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("property_quarter").split()[0]
            zone = self.cleaned_data.get("property_quarter").split()[-1]
            quarter = Quarter.objects.get(name=name, zone__name=zone)
            return quarter
        except Exception as e:
            raise forms.ValidationError("this quarter is unknown") 
