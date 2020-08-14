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
            attrs = {'placeholder': 'Giver wife name', 
                    'class': 'form-control'}),
        label = 'Giver wife name')

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

    search_place = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Place to look for the document.', 
                    'class': 'form-control',
                    'id':'search_place'}),
        label = 'Place to look for the document.',
        queryset = Quarter.objects.all())
        
    class Meta:
        model = Document
        fields = ("search_place","beneficiary","property_quarter","mrs","cnis11","cnis12","cnis21","cnis22")

    # def clean_beneficiary(self, *arg,**kwargs):
    #     try:
    #         CNI = self.cleaned_data.get("beneficiary")
    #         comparant = Profile.objects.get(CNI=CNI)
    #         return comparant
    #     except:
    #         raise forms.ValidationError("CNI does not exist")

    # def clean_cnis11(self, *arg,**kwargs):
    #     try:
    #         CNI = self.cleaned_data.get("cnis11")
    #         comparant = Profile.objects.get(CNI=CNI)
    #         return comparant
    #     except:
    #         raise forms.ValidationError("CNI does not exist")

    # def clean_cnis12(self, *arg,**kwargs):
    #     try:
    #         CNI = self.cleaned_data.get("cnis12")
    #         comparant = Profile.objects.get(CNI=CNI)
    #         return comparant
    #     except:
    #         raise forms.ValidationError("CNI does not exist")

    # def clean_cnis21(self, *arg,**kwargs):
    #     try:
    #         CNI = self.cleaned_data.get("cnis21")
    #         comparant = Profile.objects.get(CNI=CNI)
    #         return comparant
    #     except:
    #         raise forms.ValidationError("CNI does not exist")

    # def clean_cnis22(self, *arg,**kwargs):
    #     try:
    #         CNI = self.cleaned_data.get("cnis22")
    #         comparant = Profile.objects.get(CNI=CNI)
    #         return comparant
    #     except:
    #         raise forms.ValidationError("CNI does not exist")

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