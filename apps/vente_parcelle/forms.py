from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):
    zone = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Zone', 
                    'class': 'form-control', 
                    'list':'zones'}),
        label = 'Zone')
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

    buyer = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer', 
                    'class': 'form-control'}),
        label = 'Buyer')

    buyer_father = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer\'s Father', 
                    'class': 'form-control'}),
        label = 'Buyer\'s Father')

    buyer_mother = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer\'s Mather', 
                    'class': 'form-control'}),
        label = 'Buyer\'s Mather')


    buyer_zone = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer Zone', 
                    'class': 'form-control'}),
        label = 'Buyer Zone')
    
    buyer_residence_quarter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer Residence Quarter', 
                    'class': 'form-control'}),
        label = 'Buyer Residence Quarter')


    class Meta:
        model = Document
        fields = ("zone", "residence_quarter","amount","buyer","buyer_father","buyer_mother","buyer_zone")

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
    