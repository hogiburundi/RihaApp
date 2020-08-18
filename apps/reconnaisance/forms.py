from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):
        
    association_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Association Quarter', 
                    'class': 'form-control',
                    'id':'residence_quarter'}),
        label = 'Association Quarter',
        queryset = Quarter.objects.all())
        
    association = forms.CharField(
        widget = forms.TextInput(
        attrs = {'placeholder': 'Votre Association', 
                    'class': 'form-control'}),
        label = 'Votre Association')

    start_year = forms.CharField(
        widget = forms.TextInput(
        attrs = {'placeholder': 'Année de lancement', 
                    'class': 'form-control'}),
        label = 'Année de lancement')    
    
    class Meta:
        model = Document
        fields = ("association_quarter", "association", "start_year")
        
    def clean_association_quarter(self, *arg,**kwargs):
        try:
            CNI = self.cleaned_data.get("association_quarter")
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