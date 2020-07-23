from django import forms
from .models import *
from apps.base.models import *
from datetime import date

class DocumentForm(forms.ModelForm):
    zone = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Zone', 
                    'class': 'form-control', 
                    'list':'zones'}),
        label = 'Zone') 

    residence_quarter = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Quarter residence', 
                    'class': 'form-control', 
                    'list':'quarters'}),
        label = 'Residence Quarter')

    date = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(2020, date.today().year),
            attrs={'placeholder':'yyyy-mm-dd ', 'class':'form-control',
                'style':'width: auto;display: inline-block;'}),
        label='date')

    comparant_1 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Nom et Prenom du comparant', 
                    'class': 'form-control'}),
        label = 'CNI du premier comparant') 
        
    comparant_2 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Nom et Prenom du comparant', 
                    'class': 'form-control'}),
        label = 'CNI du second comparant',
        required=False) 
        
    comparant_3 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Nom et Prenom du comparant', 
                    'class': 'form-control'}),
        label = 'CNI du troisième comparant',
        required=False) 

    class Meta:
        model = Document
        fields = ("zone", "residence_quarter", "date", "comparant_1", "comparant_2","comparant_3")

    def clean_comparant_1(self, *arg,**kwargs):
        try:
            CNI = self.cleaned_data.get("comparant_1")
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("Ce comparant n'est pas abonné")

    def clean_comparant_2(self, *arg,**kwargs):
        CNI = self.cleaned_data.get("comparant_2")
        if not CNI.strip():
            return None
        try:
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("Ce comparant n'est pas abonné")

    def clean_comparant_3(self, *arg,**kwargs):
        CNI = self.cleaned_data.get("comparant_3")
        if not CNI.strip():
            return None
        try:
            CNI = self.cleaned_data.get("comparant_3")
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("Ce comparant n'est pas abonné")

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