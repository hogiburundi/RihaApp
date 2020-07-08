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

    beneficiary = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary', 
                    'class': 'form-control'}),
        label = 'Beneficiary')

    beneficiary_zone = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary origine zone', 
                    'class': 'form-control',
                    'list':'zones'}),
        label = 'Beneficiary origine zone')

    beneficiary_residence_zone = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary residence zone', 
                    'class': 'form-control',
                    'list':'zones'}),
        label = 'Beneficiary residence zone') 

    realestate_quarter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Realestate quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Realestate quarter')

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

    giv_eyewitness1 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver eyewitness 1', 
                    'class': 'form-control'}),
        label = 'Giver eyewitness 1')

    giv_eyewitness2 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver eyewitness 2', 
                    'class': 'form-control'}),
        label = 'Giver eyewitness 2')

    ben_eyewitness1 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary eyewitness 1', 
                    'class': 'form-control'}),
        label = 'Beneficiary eyewitness 1')

    ben_eyewitness2 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary eyewitness 2', 
                    'class': 'form-control'}),
        label = 'Beneficiary eyewitness 2')

    class Meta:
        model = Document
        fields = ("zone", "residence_quarter","beneficiary","beneficiary_zone","beneficiary_residence_quarter","beneficiary_residence_zone","realestate_quarter","mrs","giv_eyewitness1","giv_eyewitness2","ben_eyewitness1","ben_eyewitness2")

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

    def clean_beneficiary_zone(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("beneficiary_zone")
            zone = Zone.objects.get(name=name)
            return zone
        except:
            raise forms.ValidationError("this zone is unknown")

    def clean_beneficiary_residence_zone(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("beneficiary_residence_zone")
            zone = Zone.objects.get(name=name)
            return zone
        except:
            raise forms.ValidationError("this zone is unknown")

    def clean_realestate_quarter(self, *arg,**kwargs):
        try:
            name = self.cleaned_data.get("realestate_quarter").split()[0]
            zone = self.cleaned_data.get("realestate_quarter").split()[-1]
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