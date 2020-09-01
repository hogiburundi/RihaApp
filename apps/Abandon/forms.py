from django import forms
from datetime import date
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):
    Abandon     = forms.CharField(label="Abandon", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Abandon '}))
    tuteurAcueillantObjetAbandon      = forms.CharField(label="Tutilleur", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'tuteur acueillant l\'abandonne '}))

    zone = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Zone', 'class': 'form-control', 'id':'zones'}),
        label = 'Zone',
        queryset = Zone.objects.all())
    
    residence_quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 'class': 'form-control','id':'quarters'}),
        label = 'Residence Quarter',
        initial = Profile.residence,
        queryset = Quarter.objects.all())


    date_delivrated = forms.DateField(widget=forms.TextInput(
            attrs={'placeholder':'yyyy-mm-dd ', 'type':'date',
                'class':'form-control',}),
        initial=date.today(),
        label='Date :', required=False)


    class Meta:
        model = Document
        fields = ("zone", "residence_quarter", "Abandon", 'date_delivrated',"tuteurAcueillantObjetAbandon")

    

class ValidationForm(forms.Form):
    cni_recto = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image recto '}),
        label='image recto', required=False)
    cni_verso = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'image verso '}),
        label='image verso', required=False)
    payment = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'le code de paiement '}),
        label='le code de paiement', required=False)
    cni = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'numero CNI '}),
        label='numero CNI', required=False)