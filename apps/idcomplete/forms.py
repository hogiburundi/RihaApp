from django import forms
from .models import *
from apps.base.models import *

class DocumentForm(forms.ModelForm):
    payment_methods = (
        ('', '-------------'),
        ('ecocash', 'Ecocash'),
        ('lumicash', 'Lumicash')
    )
    
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

    payment_method = forms.ChoiceField(
        widget = forms.Select(attrs = {'placeholder': 'Payment Method', 'class': 'form-control'}),
        label = 'Payment Method',
        choices=payment_methods)
    
    payment_serial = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Payment Serial', 'class': 'form-control'}),
        label = 'Payment Serial')

    class Meta:
        model = Document
        # fields = ("zone_leader", "zone", "beneficiary", "father", "mother", "birth_quarter", "birth_year", "birth_commune", "birth_province", "nationality", "etat_civil", "proffession", "residence_quarter", "residence_zone", "CNI", "payment_method", "payment_serial")
        fields = ("zone", "residence_quarter","payment_method", "payment_serial")

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