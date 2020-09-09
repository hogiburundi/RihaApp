from django.forms import ModelForm, BaseInlineFormSet, inlineformset_factory
from .models import *
from django import forms
from apps.base.models import *
from datetime import date

class DocumentForm(ModelForm):
    quarter = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Residence Quarter', 'class': 'form-control','id':'quarters'}),
        label = 'Residence Quarter',
        queryset = Quarter.objects.all())

    conjoint = forms.CharField(widget=forms.TextInput(
            attrs={'class':'form-control check_cni',
                'placeholder':'CNI du conjoint '}),
        label="CNI du conjoint ")

    class Meta:
        model = Document
        fields = ("quarter", 'conjoint')

    def clean_conjoint(self, *arg, **kwargs):
        try:
            CNI = self.cleaned_data.get('conjoint')
            conjoint = Profile.objects.get(CNI = CNI)
            return conjoint
        except Exception as e:
            raise forms.ValidationError("Desole, le conjoint  n'existe pas!! ")

class ChildForm(ModelForm):
    name = forms.CharField( widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'nom et prenom de l\'enfant'}),
        label="Name",)
    date = forms.DateTimeField( widget=forms.SelectDateWidget(
            attrs={'class':'form-control','placeholder':'date de naissance de l\'enfant '},
            years=range(2000, date.today().year+1)),
        label="date de naissance",)
    
    class Meta:
        model = Child
        fields = ('name', 'date')

    def clean_date(self, *args, **kwargs):
        if self.cleaned_data.get('date') > date.today():
            raise forms.ValidationError("La date ne peut pas aller au delà d'aujourd'hui")
        return self.cleaned_data.get('date')
