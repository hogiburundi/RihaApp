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
            attrs = {'placeholder': 'Residence Quarter', 
                    'class': 'form-control',
                    'list':'quarters'}),
        label = 'Residence Quarter')

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



    def clean_defunt(self, *arg, **kwargs):
        try:
            CNI = self.cleaned_data.get('defunt')
            conjoint = Profile.objects.get(CNI = CNI)
            return conjoint
        except Exception as e:
            raise forms.ValidationError("Desolee, le defunt n'existe pas!! ")