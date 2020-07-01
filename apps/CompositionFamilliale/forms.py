from django import forms
from .models import *
from django.forms import formset_factory
from .models import *
from apps.base.models import *

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
    fullname_lady      = forms.CharField(
        label="Nom&Prenom du conjoint", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class':'form-control',
                                      'placeholder':'nom et prenom du conjoint '}))
    


    class Meta:
        model = Document
        fields = ("zone", "residence_quarter", 'fullname_lady')

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


class ChildForm(forms.Form):

    fullname_child      = forms.CharField(
        label="Nom&Prenom de l'enfant", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class':'form-control',
                                      'placeholder':'nom et prenom de l\'enfant'}))

ChildFormset = formset_factory(ChildForm, extra=1)