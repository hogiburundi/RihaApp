from django import forms
from .models import *
from apps.base.models import *
from datetime import date




class DocumentForm(forms.ModelForm):
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
    
    defunt    = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder' : 'Le numero de Cni du defunt',
                     'class': 'form-control'}),
        label = 'Defunt')


    date = forms.DateField(widget=forms.TextInput(
            attrs={'placeholder':'yyyy-mm-dd ', 'type':'date',
                'class':'form-control',}),
        initial=date.today(),
        label='Date de deces ')




    acte = forms.IntegerField(
            widget = forms.NumberInput(
                attrs  = {'placeholder': 'numero d\'acte' , 
                        'class': 'form-control'}),
                label = 'Acte')

            
    volume = forms.IntegerField(
            widget = forms.NumberInput(
                attrs = {'placeholder': 'numero de volume', 
                        'class': 'form-control'}),
                label = 'Volume')

            
    class Meta:
        model = Document
        fields = ("zone", "residence_quarter",'date','defunt', 'acte', 'volume' )

    



    def clean_defunt(self, *arg, **kwargs):
        try:
            CNI = self.cleaned_data.get('defunt')
            defunt = Profile.objects.get(CNI = CNI)
            return defunt
        except Exception as e:
            raise forms.ValidationError("Desolee, le defunt n'existe pas!! ")



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