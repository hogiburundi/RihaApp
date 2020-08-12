from django import forms
from .models import *
from apps.base.models import *
from django import forms

class DocumentForm(forms.ModelForm):    
    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Zone', 
                    'class': 'form-control', 
                    'id':'zones'}),
        label = 'Zone',
        queryset = Zone.objects.all())

    first_witness = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'witness', 
                    'class': 'form-control', 
                    'id':'profiles1'}),
        label = "Témoin 1 : ",
        queryset = Profile.objects.all())

    second_witness = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'witness', 
                    'class': 'form-control', 
                    'id':'profiles2'}),
        label = "Témoin 1 : ",
        queryset = Profile.objects.all())

    class Meta:
        model = Document
        fields = ("zone", "first_witness","second_witness")
        
class ValidationForm(forms.Form):
    cni_recto = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image recto '}),
        label='image recto', required=False)
    cni_verso = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image verso '}),
        label='image verso', required=False)
    cni = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'numero CNI '}),
        label='numero CNI', required=False)

    cni_recto_first_witness = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image recto témoin 1 '}),
        label='image recto', required=False)
    cni_verso_first_witness = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image verso témoin 1 '}),
        label='image verso', required=False)
    cni_first_witness = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'numero CNI témoin 1'}),
        label='numero CNI', required=False)

    cni_recto_second_witness = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image recto témoin 2 '}),
        label='image recto', required=False)
    cni_verso_second_witness = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image verso témoin 2 '}),
        label='image verso', required=False)
    cni_second_witness = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'numero CNI témoin 2'}),
        label='numero CNI', required=False)
    
    payment = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'le code de paiement '}),
        label='le code de paiement', required=False)