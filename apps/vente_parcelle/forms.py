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

    witness11 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Saler witness CNI 1',
                    'class': 'form-control'}),
        label = 'Saler witness CNI 1')  
              
    witness12 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Saler witness CNI 2',
                    'class': 'form-control'}),
        label = 'Saler witness CNI 2')
        
    witness21 = forms.CharField( 
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer witness CNI 1',
                    'class': 'form-control'}),
        label = 'Buyer witness CNI 1')

    witness22 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Buyer witness CNI 2',
                    'class': 'form-control'}),
        label = 'Buyer witness CNI 2')
        
    class Meta:
        model = Document
        fields = ("property_quarter", "amount", "buyer", "witness11", "witness12", "witness21", "witness22")

    def clean_buyer(self, *arg,**kwargs):
        try:
            CNI = self.cleaned_data.get("buyer")
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