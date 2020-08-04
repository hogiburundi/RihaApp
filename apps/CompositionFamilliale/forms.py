from django.forms import ModelForm, inlineformset_factory
from .models import *
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

   


class ChildForm(ModelForm):
    class Meta:
        model = Child
        exclude = ()
    def save(self):
        formset = Child.objects.create(
        name=self.cleaned_data['name'],
        age=self.cleaned_data['age'])
        return formset

ChildFormset = inlineformset_factory(Document, Child, 
                                form = ChildForm, extra=1)

