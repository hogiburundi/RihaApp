from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):

    beneficiary = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary CNI', 
                    'class': 'form-control'}),
        label = 'Beneficiary CNI')

    property_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Property quarter', 
                    'class': 'form-control',
                    'id':'property_quarter'}),
        label='Property quarter',
        queryset = Quarter.objects.all())

    mrs = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver wife CNI',
                    'id':'', 
                    'class': 'form-control'}),
        label = 'Giver wife CNI')  
       
    witness11 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver witness CNI',
                    'id':'', 
                    'class': 'form-control'}),
        label = 'Giver witness CNI 1')  
              
    witness12 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Giver witness CNI',
                    'id':'', 
                    'class': 'form-control'}),
        label = 'Giver witness CNI 2')
        
    witness21 = forms.CharField( 
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary witness CNI',
                    'id':'', 
                    'class': 'form-control'}),
        label = 'Beneficiary witness CNI 1')

    witness22 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Beneficiary witness CNI',
                    'id':'', 
                    'class': 'form-control'}),
        label = 'Beneficiary witness CNI 2')

    class Meta:
        model = Document
        fields = ("beneficiary","property_quarter","mrs","witness11","witness12","witness21","witness22")

    def clean_beneficiary(self, *arg,**kwargs):
        try:
            CNI = self.cleaned_data.get("beneficiary")
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("CNI does not exist")

    def clean_mrs(self, *arg,**kwargs):
        try:
            CNI = self.cleaned_data.get("mrs")
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("CNI does not exist")

    def clean_witness11(self, *arg,**kwargs):
        try:
            CNI = self.cleaned_data.get("witness11")
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("CNI does not exist")

    def clean_witness12(self, *arg,**kwargs):
        try:
            CNI = self.cleaned_data.get("witness12")
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("CNI does not exist")

    def clean_witness21(self, *arg,**kwargs):
        try:
            CNI = self.cleaned_data.get("witness21")
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("CNI does not exist")

    def clean_witness22(self, *arg,**kwargs):
        try:
            CNI = self.cleaned_data.get("witness22")
            comparant = Profile.objects.get(CNI=CNI)
            return comparant
        except:
            raise forms.ValidationError("CNI does not exist")

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
        