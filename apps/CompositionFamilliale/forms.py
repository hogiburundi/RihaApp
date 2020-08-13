from django.forms import ModelForm, BaseInlineFormSet, inlineformset_factory
from .abc import is_empty_form, is_form_persisted
from .models import *
from django import forms
from apps.base.models import *

class DocumentForm(ModelForm):

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

    conjoint      = forms.CharField(
        label="Conjoint",
        widget=forms.TextInput(attrs={'class':'form-control',
                                      'placeholder':'numero de CNI du conjoint '}))
    


    class Meta:
        model = Document
        fields = ("zone", "residence_quarter", 'conjoint')



    def clean_conjoint(self, *arg, **kwargs):
        try:
            CNI = self.cleaned_data.get('conjoint')
            conjoint = Profile.objects.get(CNI = CNI)
            return conjoint
        except Exception as e:
            raise forms.ValidationError("Desole, le conjoint  n'existe pas!! ")




# 
class ChildForm(ModelForm):

    name      = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={'class':'form-control',
                                      'placeholder':'nom et prenom de l\'enfant'}))
    

    age      = forms.IntegerField(
        label="Age",
        widget=forms.NumberInput(attrs={'class':'form-control',
                                      'placeholder':'age de l\'enfant '}))
    

    class Meta:
        model = Child
        fields = ('name', 'age')
