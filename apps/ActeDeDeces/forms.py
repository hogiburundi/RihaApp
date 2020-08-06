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
        queryset = Quarter.objects.all())

    defunt    = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder' : 'Le numero de Cni du defunt',
                     'class': 'form-control'}),
        label = 'Defunt')


    date = forms.DateField(
        widget = forms.SelectDateWidget(
            attrs = {'placeholder': 'date' , 
                    'class': 'form-control',
                    'style': 'display:inline-block; width: auto'}),
            label = 'date')



    acte = forms.IntegerField(
            widget = forms.NumberInput(
                attrs = {'placeholder': 'numero d\'acte' , 
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
            conjoint = Profile.objects.get(CNI = CNI)
            return conjoint
        except Exception as e:
            raise forms.ValidationError("Desolee, le defunt n'existe pas!! ")