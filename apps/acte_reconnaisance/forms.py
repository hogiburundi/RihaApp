from django import forms
from .models import *
from apps.base.models import *
from datetime import date

class DocumentForm(forms.ModelForm):
        
    volume = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Volume', 
                    'class': 'form-control'}),
        label = 'Volume')
        
    acte = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Acte', 
                    'class': 'form-control'}),
        label = 'Acte')
        
    day_month_year = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1950, date.today().year+1),
            attrs={'placeholder':'yyyy-mm-dd ', 'class':'form-control',
                'style':'width: 50%;'}),
        label='Day')

    child_date = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1950, date.today().year+1),
            attrs={'placeholder':'yyyy-mm-dd ', 'class':'form-control',
                'style':'width: 50%;display:'}),
        label='Child Day')

    search_place = forms.ModelChoiceField(
        widget = forms.Select(
            attrs = {'placeholder': 'Place to look for the document.', 
                    'class': 'form-control',
                    'id':'search_place'}),
        label = 'Place to look for the document.',
        queryset = Quarter.objects.all())

    cnis11 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'First Witness CNI',
                    'class': 'form-control'}),
        label = 'First Witness CNI')  
              
    cnis12 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Second Witness CNI',
                    'class': 'form-control'}),
        label = 'Second Witness CNI')
        
    cnis13 = forms.CharField( 
        widget = forms.TextInput(
            attrs = {'placeholder': 'Child CNI',
                    'class': 'form-control'}),
        label = 'Child CNI')

    cnis14 = forms.CharField(
        widget = forms.TextInput(
            attrs = {'placeholder': 'Wife CNI',
                    'class': 'form-control'}),
        label = 'Wife CNI')


    class Meta:
        model = Document
        fields = ("search_place", "volume", "acte", "day_month_year", "child_date","cnis11","cnis12","cnis13","cnis14")


class ValidationForm(forms.Form):
    cni_recto = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI recto', required=False)
    cni_verso = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI verso', required=False)
    cni_recto_1 = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI recto comparant 1', required=False)
    cni_verso_1 = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI verso comparant 1', required=False)
    cni_recto_2 = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI recto comparant 2', required=False)
    cni_verso_2 = forms.BooleanField(widget=forms.CheckboxInput(),
        label='CNI verso comparant 2', required=False)
    payment = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'le code de paiement '}),
        label='le code de paiement', required=False)
    cni = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'placeholder':'numero CNI '}),
        label='numero CNI', required=False)